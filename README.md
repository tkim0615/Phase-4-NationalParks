# Communcating With the Server Lecture

## 1. Design a DB that mimics the given schema
-     Hint: `server_default = db.func.now()` and `onupdate = db.func.now()`
## 2. Add relationships to reflect the to-many aspect of the DB
-     Hint: `back_populates`
-     Hint: How do we deal with the inherent recursivity of these relationships?
## 3. Add the following validation to the User model:
##      username attribute must have between 4 and 14 characters, inclusive
##      otherwise, raise a value error
## 4. Create, migrate, and seed the DB
-     Hint: `flask db init`, `flask db migrate -m ""`, `flask db upgrade`
-     Hint: How can we use the given seed file?
## 5. Build out the following RESTful CRUD backend routes and test:
##      GET '/users'
##      GET '/national_parks'
##      GET '/users/\<int:id>'
##      POST '/users'
##      PATCH '/users/\<int:id>'
##      DELETE '/national_parks/\<int:id>'
-     Hint: How do we account for validations?