from werkzeug.exceptions import NotFound

from . import bp_obj, views
from project.core.models import User


@bp_obj.route('/')
def index():

    return 'Welcome home.'


@bp_obj.route('/users/<username>')
def get_profile_info(username):

    user = User.query.filter(User.username == username).first()

    if user is None:
        raise NotFound('User not found.')

    return views.json_serialise_user(user)
