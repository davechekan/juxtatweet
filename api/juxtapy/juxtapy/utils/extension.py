
import flask.ext.sqlalchemy as sqla

def setup_sqlalchemy(app):
    """
    Set up the sqlalchemy extension, and return it. All configuration
    is handled by the config package.
    """

    db = sqla.SQLAlchemy(app)
    return db

