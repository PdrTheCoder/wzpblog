from sqlalchemy.exc import IntegrityError
from flask import jsonify

def register_err_handler(app):
    @app.errorhandler(Exception)
    def handle_all_exceptions(e):
        message = "An Internal error which we don't expect occurred"

        # Handle SQLAlchemy IntegrityError
        if isinstance(e, IntegrityError):
            message = "Sql integrity error occurred, I am sorry."
        
        return jsonify({
            "code": -1,
            "msg": message,
            "data": None
        })