from main.views import blue,init_model


local_db_uri = 'mysql://yb:980708@127.0.0.1:3306/db'
remote_db_uri = 'mysql://yb:980708@39.107.109.101:3001/db'

def create_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = remote_db_uri
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    app.register_blueprint(blue)
    init_model(app)
    return app
