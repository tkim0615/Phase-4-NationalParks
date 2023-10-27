from flask import request, make_response, jsonify

from werkzeug.exceptions import NotFound

from config import app

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