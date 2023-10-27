from flask import request, make_response

from werkzeug.exceptions import NotFound

from config import app

# unique error message upon nonexistent server-side route
@app.errorhandler(NotFound)
def route_not_found(e):
    response = make_response(
        "That route does not exist!",
        404
    )
    
    return response

@app.route('/')
def home():
    return ""

if __name__ == '__main__':
    app.run(port = 5555, debug = True)