from application import db
from utilities import utc_now_ts as now

class User(db.Document):
    username = db.StringField(db_field="u", required=True)
    password = db.StringField(db_field="p",required=True)
    email = db.EmailField(db_field="e",required=True)
    firstname=db.StringField(db_field="fn",max_length=50)
    lastname=db.StringField(db_field="ln",max_length=50)
    created=db.IntField(db_field="c",default=now())
