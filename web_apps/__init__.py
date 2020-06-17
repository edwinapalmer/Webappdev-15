from flask import Flask

from web_apps.models import db, migrate
from web_apps.routes.home_routes import home_routes
from web_apps.routes.tweet_routes import tweet_routes
from web_apps.services.basilica_service import connnection

DATABASE_URI = "sqlite:///web_apps_99.db" # using relative filepath
#DATABASE_URI = "sqlite:////Users/Username/Desktop/your-repo-name/web_app_99.db" # using absolute filepath on Mac (recommended)
#DATABASE_URI = "sqlite:///C:\\Users\\Username\\Desktop\\your-repo-name\\web_app_99.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(tweet_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)


