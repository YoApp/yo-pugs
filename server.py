# -*- coding: utf-8 -*-
import random
from flask import Flask, render_template, request, session, redirect
import requests
import os
from user_agents import parse
from yo import Yo


app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

yo = Yo(client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        redirect_uri=os.environ.get('REDIRECT_URI'))

if not yo.client_id or \
        not yo.client_secret or \
        not yo.redirect_uri:
    print 'Yo, you need to set your client straight: https://dashboard.justyo.co'
    exit(1)


def fetch_random_gif(keyword):
    giphy_result = requests.get('http://api.giphy.com/v1/gifs/search?q=%s&api_key=dc6zaTOxFJmzC' % keyword)
    data = giphy_result.json()['data']
    urls = [item['images']['original']['url'] for item in data]
    random_url = random.choice(urls)
    return random_url


@app.route('/')
def home():

    keyword = os.environ.get('GIPHY_KEYWORD', 'pug')
    random_gif_url = fetch_random_gif(keyword)

    user_agent = parse(request.headers.get('User-Agent'))

    if session.get('access_token'):

        yo.access_token = session.get('access_token')

        contacts = yo.fetch_contacts()
        if contacts is None:
            session.pop('access_token', None)
            return redirect('/')

        colors = [
            'turquoise',
            'emerald',
            'peter',
            'asphalt',
            'green',
            'sunflower',
            'belize',
            'wisteria'
        ]

        return render_template('index.html', contacts=contacts, colors=colors, background_url=random_gif_url,
                               is_mobile=user_agent.is_mobile)
    else:
        url_for_authorize = yo.url_for_authorize()
        return render_template('login.html', url_for_authorize=url_for_authorize, background_url=random_gif_url,
                               is_mobile=user_agent.is_mobile)


@app.route('/yo', methods=['POST'])
def send_yo():
    yo.access_token = session.get('access_token')
    response = yo.send(username=request.form.get('username'),
                       link=request.form.get('link'),
                       response_pair=u'🐶.😂')
    print response.status_code, response.text
    return response.text


@app.route('/logout')
def logout():
    session.pop('access_token', None)
    return redirect('/')


@app.route('/authorized')
def authorized():
    access_token = yo.exchange_code_for_access_token(request.args.get('code'))
    session['access_token'] = access_token
    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.secret_key = os.environ.get('SECRET_KEY')
    port = int(os.environ.get('PORT', 8000))
    app.run(host="0.0.0.0", port=port)
