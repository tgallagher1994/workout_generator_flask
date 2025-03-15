from flask import Flask
from app_routes import app_routes  # Import Blueprint correctly

app = Flask(__name__)
app.register_blueprint(app_routes)  # Register Blueprint

if __name__ == "__main__":
    app.run(debug=True)
