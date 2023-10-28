from app import app
from models import db, User, NationalPark, UserVisitedPark

if __name__ == '__main__':
    with app.app_context():

        User.query.delete()
        NationalPark.query.delete()
        UserVisitedPark.query.delete()

        # seed 3 users
        users_to_add = []

        users_to_add.append(User(
            id = 1,
            username = "jenny123",
            password = "p4$$w0rd"
        ))

        users_to_add.append(User(
            id = 2,
            username = "Carl",
            password = "xsecurexpasswordx"
        ))

        users_to_add.append(User(
            id = 3,
            username = "4vicky86",
            password = "abcABC"
        ))

        db.session.add_all(users_to_add)

        # seed 2 national parks
        parks_to_add = []

        parks_to_add.append(NationalPark(
            id = 1,
            name = "Zion National Park",
            state = "Utah"
        ))

        parks_to_add.append(NationalPark(
            id = 2,
            name = "Grand Canyon National Park",
            state = "Arizona"
        ))

        db.session.add_all(parks_to_add)

        db.session.commit()

        # seed 3 visits
        visits_to_add = []

        visits_to_add.append(UserVisitedPark(
            id = 1,
            date_of_visit = "04/20/2018",
            user_id = 2,
            park_id = 1
        ))

        visits_to_add.append(UserVisitedPark(
            id = 2,
            date_of_visit = "11/03/2016",
            user_id = 2,
            park_id = 2
        ))

        visits_to_add.append(UserVisitedPark(
            id = 3,
            date_of_visit = "01/14/2018",
            user_id = 1,
            park_id = 1
        ))

        db.session.add_all(visits_to_add)

        db.session.commit()
        