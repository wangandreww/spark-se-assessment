from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class UsersAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):

        emails = []

        users = User.query.all()
        for user in users:
            emails.append(user.email)
        
        for email in emails:
            print(email)
        
        responseObject = {
            "users" : emails
            
        }
        return make_response(jsonify(responseObject)), 201

    # def post(self):
    #     # get the post data
    #     post_data = request.get_json(); print(request)
    #     # check if user already exists
    #     user = User.query.filter_by(email=post_data.get('email')).first()
    #     if not user:
    #         try:
    #             user = User(
    #                 email=post_data.get('email'),
    #                 password=post_data.get('password')
    #             )

    #             # insert the user
                
    #             db.session.add(user)
                
    #             db.session.commit()
                
    #             # generate the auth token
    #             auth_token = user.encode_auth_token(user.id)
    #             print(auth_token)
    #             responseObject = {
    #                 'status': 'success',
    #                 'message': 'Successfully registered.',
    #                 'auth_token': auth_token
    #             }
    #             return make_response(jsonify(responseObject)), 201
    #         except Exception as e:
    #             responseObject = {
    #                 'status': 'fail',
    #                 'message': 'Some error occurred. Please try again.'
    #             }
    #             return make_response(jsonify(responseObject)), 401
    #     else:
    #         responseObject = {
    #             'status': 'fail',
    #             'message': 'User already exists. Please Log in.',
    #         }
    #         return make_response(jsonify(responseObject)), 202


# define the API resources
users_view = UsersAPI.as_view('user_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=users_view,
    methods=['GET']
)


