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