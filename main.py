from flask import Flask
from data import db_session
from flask import render_template
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    db_sess = db_session.create_session()

    # user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"
    #
    # user1 = User()
    # user1.surname = "Tom"
    # user1.name = "Clinton"
    # user1.age = 19
    # user1.position = "soldier"
    # user1.speciality = "research engineer"
    # user1.address = "module_3"
    # user1.email = "tom_clin_boy@mars.org"
    #
    # user2 = User()
    # user2.surname = "Mike"
    # user2.name = "Tomson"
    # user2.age = 20
    # user2.position = "soldier"
    # user2.speciality = "doctor"
    # user2.address = "module_2"
    # user2.email = "mike_med@mars.org"
    #
    # user3 = User()
    # user3.surname = "Gon"
    # user3.name = "Hanley"
    # user3.age = 21
    # user3.position = "soldier"
    # user3.speciality = "mars driver"
    # user3.address = "module_5"
    # user3.email = "drive_live_gon@mars.org"
    #
    # db_sess.add(user3)
    # db_sess.add(user2)
    # db_sess.add(user1)
    # db_sess.add(user)
    # db_sess.commit()

    # job = Jobs(user_id=1)
    # job.team_leader = 1
    # job.job = 'deployment of residential modules 1 and 2'
    # job.work_size = 15
    # job.collaborators = '2, 3'
    # # job.start_date
    # job.is_finished = False
    #
    # db_sess.add(job)
    # db_sess.commit()


if __name__ == '__main__':
    main()