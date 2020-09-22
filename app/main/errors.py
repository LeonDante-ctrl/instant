from flask import render_template
from . import main

#error handler
@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    function to render the 404 error page
    '''
    title = '404 page'
    return render_template('fourOwFour.html', title=title), 404
