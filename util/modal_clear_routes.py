from flask import session, Blueprint

modal_clear = Blueprint('modal_clear', __name__)

@modal_clear.route('/clear-logout-flag')
def clear_logout_flag():
    session.pop('logged_out', None)
    return '', 204
