


MEETUP_LIST = []

class Meetup():
    def create_meetup(self, meetup_id, createdOn, location, images, topic, happeningOn, tags):
        self.single_meet = {}

        self.single_meet[meetup_id] = meetup_id
        self.single_meet[createdOn] = createdOn
        self.single_meet[location] = location
        self.single_meet[images] = images
        self.single_meet[topic] = topic
        self.single_meet[happeningOn] = happeningOn
        self.single_meet[tags] = tags

        MEETUP_LIST.append(self.single_meet)
        return {
                            "status": 201,
                            "data": self.single_meet
        }
