
Send Pug gifs to your Yo buddies!

![](http://cl.ly/image/1C252V3M2037/yo-pugs.gif)
[http://docs.justyo.co/v2.0/docs/](http://docs.justyo.co/v2.0/docs/)

Specify the response on the notification from your code!

![](http://cl.ly/image/3S362I430J0d/Untitled.png)

## Getting Started

* Install [pip](http://pip.readthedocs.org/en/latest/installing.html) package manager if you haven't yet:

        Linux: sudo apt-get install python-pip
        Mac: brew install python

* Install [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation):

        sudo pip install virtualenv

* Clone this repo: 

        git clone git@github.com:YoApp/yo-pugs.git
        cd yo-pugs
        
* Create a virtualenv, activate it and install dependencies:

        virtualenv env
        . env/bin/activate
        pip install -r requirements.txt

* Login or signup using your personal account to https://dev.justyo.co/
![Create client](http://cl.ly/image/3S2u2U0X0H0d/Screen%20Shot%202015-07-27%20at%201.37.00%20PM.png)

* Create a new Yo app (Yo OAuth Client) 
![Create client](http://cl.ly/image/2S1O2w2f0i0B/Create%20new%20client.png)

* Great! You created your Yo client! Here are the things you'll need to get started:
![View new client](http://cl.ly/image/2f1E3y2Y2H3r/View%20new%20client%20info_censored.jpg)

* Generate a secret key for your flask app to store sessions in a secure way:  

You can use this [online password generator](https://www.random.org/passwords/?num=1&len=24&format=plain)  

* Export your client id, secret and redirect uri to environment variables [(why?)](http://12factor.net/config):

        export CLIENT_ID=<your client id>
        export CLIENT_SECRET=<your client id>
        export REDIRECT_URI=<your redirect uri>
        export SECRET_KEY=<your secret key from the step above>
        export GIPHY_KEYWORD=PUGS

* Run the server:

        python server.py

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

[Apply for our Yo Developer Program](https://yoapp.typeform.com/to/xi0WMz)
