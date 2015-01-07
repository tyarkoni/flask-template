from my_app.config import settings
from my_app.app import app, setup_logging, create_app

# set up the flask app
create_app()

# set up logging
setup_logging(logging_path=settings.LOGGING_PATH,
              level=settings.LOGGING_LEVEL)

if __name__ == "__main__":
    app.run(debug=app.debug, port=5001)
