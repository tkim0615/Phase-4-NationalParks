from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

# necessary for FK constraint upgrades in alembic migrations
metadata = MetaData(naming_convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# creates SQLAlchemy DB ORM
db = SQLAlchemy(metadata = metadata)


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String, nullable=False)
    password= db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #add relation
    user_visited_parks = db.relationship('UserVisitedPark', back_populates='user', cascade = 'all, delete')

    #add serializer
    serialize_rules=('-user_visited_parks.user',)

    #add validation
    @validates('username')
    def validate_username(self, key, value):
        if not 4<=len(value)<=14:
            raise ValueError('username must be of length 4 to 14 inclusive')
        return value

class NationalPark(db.Model, SerializerMixin):
    __tablename__ = 'national_parks'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    state= db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #add relation
    user_visited_parks = db.relationship('UserVisitedPark', back_populates='national_park', cascade = 'all, delete')


    #add serializer
    serialize_rules=('-user_visited_parks.national_park',)


class UserVisitedPark(db.Model, SerializerMixin):
    __tablename__ = 'user_visited_parks'

    id = db.Column(db.Integer, primary_key=True)
    date_of_visit = db.Column(db.String)

    #add relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    park_id = db.Column(db.Integer, db.ForeignKey('national_parks.id'))

    user = db.relationship('User', back_populates='user_visited_parks')
    national_park = db.relationship('NationalPark', back_populates='user_visited_parks')

    #add serializer
    serialize_rules=('-user.user_visited_parks', '-national_park.user_visited_parks')



    










    