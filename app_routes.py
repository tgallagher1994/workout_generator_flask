from flask import Blueprint, render_template, request, jsonify

# Define the Blueprint
app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/")
def home():
    return render_template("index.html")

@app_routes.route("/build-workout", methods=["POST"])
def build_workout():
    data = request.json
    return jsonify({"workout": f"Generated workout for {data['preferences']}"})
