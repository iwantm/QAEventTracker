from application import db
from application.models import Users, Events, Group
db.drop_all()
db.create_all()