from flask import request, make_response

from werkzeug.exceptions import NotFound
from flask_restful import Api, Resource
from models import db, User, NationalPark, UserVisitedPark


from config import app
api = Api(app)

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
    return "home"


class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)
    def post(self):
        data = request.get_json()
        try:
            new_user = User(
                username = data['username'],
                password= data['password']
            )
            db.session.add(new_user)
            db.session.commit()
            return make_response(new_user.to_dict(rules=('-user_visited_parks',)), 201)

        except ValueError:
            return make_response({
                'error': 'validation error'
            })


class NationalParks(Resource):
    def get(self):
        national_parks = [park.to_dict() for park in NationalPark.query.all()]
        return make_response(national_parks, 200)
    
class UsersById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            return make_response(user.to_dict(), 200)

        else:
            return make_response({
                'Error': 'No user found'
            }, 404)


    def patch(self, id):
        user = User.query.filter(User.id == id).first()
        if user:
            try:
                data = request.get_json()
                for attr in data:
                    setattr(user, attr, data[attr])
                db.session.commit()
                return make_response(user.to_dict(), 202)
            except ValueError:
                return make_response({
                    'error': 'Validation error'
                }, 400)
        else:
            return make_response({
                'error': 'no user found'
            }, 404)

class NationalParksById(Resource):
    def delete(self, id):
        park = NationalPark.query.filter(NationalPark.id == id).first()
        if park:
            db.session.delete(park)
            db.session.commit()
            return make_response({}, 204)
        return make_response({
            'error': 'no national park found'
        }, 404)




api.add_resource(NationalParksById, '/national_parks/<int:id>')
api.add_resource(UsersById, '/users/<int:id>')
api.add_resource(NationalParks, '/national_parks')
api.add_resource(Users, '/users')



if __name__ == '__main__':
    app.run(port = 5556, debug = True)