from flask import Flask
from app.config import load_configurations, configure_logging
from .views import webhook_blueprint


def create_app():
    app = Flask(__name__)

    # Load configurations and logging settings
    load_configurations(app)
    # Print configuration values to verify
    print("ACCESS_TOKEN:", app.config["ACCESS_TOKEN"])
    print("YOUR_PHONE_NUMBER:", app.config["YOUR_PHONE_NUMBER"])
    print("APP_ID:", app.config["APP_ID"])
    print("APP_SECRET:", app.config["APP_SECRET"])
    print("RECIPIENT_WAID:", app.config["RECIPIENT_WAID"])
    print("VERSION:", app.config["VERSION"])
    print("PHONE_NUMBER_ID:", app.config["PHONE_NUMBER_ID"])
    print("VERIFY_TOKEN:", app.config["VERIFY_TOKEN"])
    configure_logging()

    # Import and register blueprints, if any
    app.register_blueprint(webhook_blueprint)

    return app
