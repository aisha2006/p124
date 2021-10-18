# Import jsonify, Flask and request from the flask.
from flask import Flask, jsonify, request

# Create an app using a flask constructor.
app = Flask(__name__)

# Create a list of contacts.
contacts = [
    {
        "data": [
            {
                "Contact": "9987644456",
                "Name": "Raju",
                "done": False,
                "id": 1
            },
            {
                "Contact": "9876543222",
                "Name": "Rahul",
                "done": False,
                "id": 2
            }
        ]

}]

# Create a route with ‘add-data’ route with POST method.
@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/add-data", methods=["POST"])
# Create a add_task() function.
def add_task():
    # Write a condition to return a message if the request is unsuccessful.
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"

        },400)
    # Create a contact dictionary with keys id , name , contact and done.
    contact = {
        "id":contacts[-1]["id"]+1,
        "Name":request.json["name"],
        "Contact":request.json.get("Contact", ""),
        "done":False
    }
    # Append the contact to list and return a json object with status successful and a message saying task added successfully.
    contacts.append(contact)
    return jsonify({"status":"success", "message":"contact added successfully"})
