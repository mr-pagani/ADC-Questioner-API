QUESTION_LIST = []


class Question():
    def create_question(
                        self, question_id, createdOn, createdBy, meetup, title,
                        body, votes):
        self.single_query = {}
        self.single_query['question_id'] = question_id
        self.single_query['createdOn'] = createdOn
        self.single_query['createdBy'] = createdBy
        self.single_query['meetup'] = meetup
        self.single_query['title'] = title
        self.single_query['body'] = body
        self.single_query['votes'] = votes

        QUESTION_LIST.append(self.single_query)

        return {"status": 201,
                "data": self.single_query
                }

    def view_questions(self):
        if len(QUESTION_LIST) == 0:
            return {"status": 404,
                    "message": "questions not found"
                    }
        else:
            return {
                    "status": 200,
                    "data": QUESTION_LIST
                    }
