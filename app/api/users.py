from app import flask_app


@flask_app.route('/api/v1.0/users/<int:id>', methods=['GET'])
def get_user(id):
    pass


@flask_app.route('/api/v1.0/users', methods=['GET'])
def get_users():
    return "Get users"


@flask_app.route('/api/v1.0/users/<int:id>/followers', methods=['GET'])
def get_followers(id):
    pass


@flask_app.route('/api/v1.0/users/<int:id>/followed', methods=['GET'])
def get_followed(id):
    pass


@flask_app.route('/api/v1.0/users', methods=['POST'])
def create_user():
    pass


@flask_app.route('/api/v1.0/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass
