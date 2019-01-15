import json
from .base_test import BaseTestCase


class TestMeetups(BaseTestCase):

    def test_post_meetups(self):
        '''post a meetup'''
        with self.client:
            response = self.client.post(
                'api/v1/meetups', data=json.dumps(dict(
                    meetup_id=2,
                    createdOn='12 SEP 2019',
                    location='nairobi',
                    images='img.url',
                    topic='interesting topic',
                    happeningOn='15 SEP 2019',
                    tags='INTERESTING'
                )),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 201)


    def test_view_meetups(self):
        response = self.client.get('/api/v1/meetups')
        self.assertEqual(response.status_code, 200)
