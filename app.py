from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# Welcome route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Event Management API"
    })


# Get all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])


# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():

    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()

    # Check if title was provided
    if not data or "title" not in data:
        return jsonify({
            "error": "Title is required"
        }), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Generate a new ID
    new_id = max([event.id for event in events], default=0) + 1

    # Create the new event
    new_event = Event(new_id, data["title"])

    # Add the event to the in-memory database
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201


# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):

    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()

    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Find the event with the requested ID
    event = None

    for item in events:
        if item.id == event_id:
            event = item
            break

    # Check if event exists
    if event is None:
        return jsonify({
            "error": "Event not found"
        }), 404

    # Check if title was provided
    if not data or "title" not in data:
        return jsonify({
            "error": "Title is required"
        }), 400

    # Update the title
    event.title = data["title"]

    # TODO: Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200


# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):

    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Find the event with the requested ID
    event = None

    for item in events:
        if item.id == event_id:
            event = item
            break

    # Check if event exists
    if event is None:
        return jsonify({
            "error": "Event not found"
        }), 404

    # Remove the event from the list
    events.remove(event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify({
        "message": "Event deleted successfully"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)