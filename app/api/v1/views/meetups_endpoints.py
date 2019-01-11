from flask import Flask, jsonify, request, Blueprint, json

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
def view_meet():
    meetups = jsonify(meetup_object.view_meetups())
    return meetups
