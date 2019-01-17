import json
from .base_test import BaseTestCase


class TestQuestions(BaseTestCase):
    def test_post_question(self):
        with self.client:
            response = self.client.post(
                '/api/v1/questions', data=json.dumps(dict(
                    question_id=100,
                    createdOn='12 APR 2019',
                    createdBy='new',
                    meetup=5,
                    title='A new question',
                    body='very long body description',
                    votes=10

                )),
                content_type='application/json'

            )

            self.assertEqual(response.status_code, 201)

    def test_get_all_questions(self):
        with self.client:
            response = self.client.post(
                '/api/v1/questions', data=json.dumps(dict(
                    question_id=100,
                    createdOn='12 APR 2019',
                    createdBy='new',
                    meetup=5,
                    title='A new question',
                    body='very long body description',
                    votes=10

                )),
                content_type='application/json'

            )

            response = self.client.get(

                '/api/v1/questions')
            self.assertEqual(response.status_code, 200)

    def test_get_question_by_id(self):
        with self.client:

            self.client.post(
                '/api/v1/questions', data=json.dumps(dict(
                    question_id=100,
                    createdOn='12 APR 2019',
                    createdBy='new',
                    meetup=5,
                    title='A new question',
                    body='very long body description',
                    votes=10

                )),
                content_type='application/json'

            )
            # Test successful get question by id
            response = self.client.get(
                '/api/v1/questions/100')
            self.assertEqual(response.status_code, 200)

            # Test get product that doesn't exist
            response1 = self.client.get(
                '/api/v1/questions/400')
            resp = json.loads(response1.data)
            self.assertEqual(
                "Question with the given id not found", resp["error"])

    def test_delete_question(self):
        with self.client:

            self.client.post(
                '/api/v1/questions', data=json.dumps(dict(
                    question_id=100,
                    createdOn='12 APR 2019',
                    createdBy='new',
                    meetup=5,
                    title='A new question',
                    body='very long body description',
                    votes=10

                )),
                content_type='application/json'

            )

            response = self.client.delete('/api/v1/questions/100')
            resp = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                "Question successfuly deleted", resp["Message"])

    def test_upvote_question(self):
        pass

    def test_downvote_question(self):
        pass
