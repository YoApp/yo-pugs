
$( "span" )
    .mouseup(function() {
        var spinner = new Spinner().spin()
        $(this).parent().append(spinner.el);
        $(this).hide();
        var name = $(this).text();
        var username = $(this).data('username');
        var link = $('body').css('background-image');
        link = link.replace('url(','').replace(')','');
        $.ajax({
            context: this,
            type: "POST",
            url: 'yo',
            data: {
                username: username,
                link: link
            },
            success: function(response) {

                spinner.stop();
                $(this).text('Sent Yo!');
                $(this).show();

                var me = $(this);
                setTimeout(
                    function(){
                        me.text(name);
                    },
                    2000
                );

            },
            error: function(error) {

                spinner.stop();
                console.log(error);

                $(this).text('Failed 😔');
                $(this).show();

                var me = $(this);
                setTimeout(
                    function(){
                        me.text(name);
                    },
                    2000
                );
            }
        });
    });