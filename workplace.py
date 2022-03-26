from data import db_session
from data.users import User
from data.jobs import Jobs


db_session.global_init("db/mars_explorer.db")
db_sess = db_session.create_session()
for user in db_sess.query(User).filter(User.age < 21, User.address == 'module_1'):
    user.address = 'module_3'
    db_sess.commit()