from flask import request, Blueprint, Response, json
from ..models import question_model

question = Blueprint('question', __name__, url_prefix='/api/v1')

question_object = question_model.Question()


@question.route('/questions', methods=['POST'])
def post_question():
    request_data = request.get_json()

    question_id = request_data.get("question_id")
    createdOn = request_data.get("createdOn")
    createdBy = request_data.get("createdBy")
    meetup = request_data.get("meetup")
    title = request_data.get("title")
    body = request_data.get("body")
    votes = request_data.get("votes")

    resp = json.dumps(question_object.create_question(
        question_id, createdOn, createdBy, meetup, title, body, votes))

    x = json.loads(resp)
    if x['status'] == 404:
        return Response(resp, 404, mimetype='application/json')
    else:
        return Response(resp, 201, mimetype='application/json')
