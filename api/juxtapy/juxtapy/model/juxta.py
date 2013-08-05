from juxtapy import db

from model_utils import dictutils
import datetime

class Juxta(db.Model):

    __tablename__ = 'juxta'

    id = db.Column(db.Integer, primary_key=True)
    #account_id = FUTURE
    tweet_url   = db.Column(db.Unicode(4096))   # how long does this need to be?
    image_url   = db.Column(db.Unicode(4096))   # how long does this need to be?

    # FIXME: All other bookkeeping shit about tweets/images

    deleted      =  db.Column(db.Boolean, default=False)
    #deleted_by   =  db.Column(db.Integer)
    deleted_date =  db.Column(db.DateTime)

    modified     =  db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created      =  db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        attrs = ('id', 'tweet_url', 'image_url', )
        return dictutils.build_dict(self, attrs)
