from application import db, pwd_context
from ..utilities import utc_now_ts as now

ACCESS_ROLES = ['developer','member', 'super_admin']

class User(db.Document):
    username = db.StringField(db_field="u", required=True, unique=True)
    password = db.StringField(db_field="p", required=True)
    email = db.EmailField(db_field="e", required=True, unique=True)
    mobile = db.StringField(db_field="mob", required=True, unique=True)
    firstname = db.StringField(db_field="fn", max_length=50)
    lastname = db.StringField(db_field="ln", max_length=50)
    created = db.IntField(db_field="c", default=now())

    def check_role(self, role):
        if role in self.roles:
            return True
        return False

    def set_password(self, password):
        self.password = pwd_context.hash(password)

    def check_password(self, password):
        return pwd_context.verify(password, self.password)
    @property
    def is_admin(self):
        return True if "super_admin" in self.roles else False

    meta = {
        'indexes': ['username', 'email', '-created']
    }