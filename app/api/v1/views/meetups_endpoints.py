from flask import jsonify, request, Blueprint
from ..models import meetup_model

meetup = Blueprint('meetup', __name__, url_prefix='/api/v1')

meetup_object = meetup_model.Meetup()


@meetup.route('/meetups', methods=['POST'])
def post_meet():
    request_data = request.get_json()

    meetup_id = request_data.get("meetup_id")
    createdOn = request_data.get("createdOn")
    location = request_data.get("location")
    images = request_data.get("images")
    topic = request_data.get("topic")
    happeningOn = request_data.get("happeningOn")
    tags = request_data.get("tags")

    response = jsonify(meetup_object.create_meetup(
        meetup_id, createdOn, location, images, topic, happeningOn, tags))

    return response


@meetup.route('/meetups')
def view_meets():
    meetups = jsonify(meetup_object.view_meetups())
    return meetups


@meetup.route('/meetups/upcoming')
def view_upcoming():
    up_meets = jsonify(meetup_object.get_upcoming())
    return up_meets


@meetup.route('/meetups/<meetup_id>')
def view_meet(meetup_id):
    meet = jsonify(meetup_object.get_meetup(meetup_id))
    return meet
