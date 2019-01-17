# ADC-Questioner-API

Badges
---------------
[![Build Status](https://travis-ci.org/mr-pagani/ADC-Questioner-API.svg?branch=develop)](https://travis-ci.org/mr-pagani/ADC-Questioner-API)  [![Coverage Status](https://coveralls.io/repos/github/mr-pagani/ADC-Questioner-API/badge.svg?branch=develop&service=github)](https://coveralls.io/github/mr-pagani/ADC-Questioner-API?branch=develop)  [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)

Summary
---------------
Questioner is a platform that allows users to crowd-source questions for meetups. The admin creates meetups, and users can post questions on specific meetups.

Questioner allows the meetup organizer to prioritize the questions to be answered. Other users can vote on the asked questions, and they bubble to the top or bottom of the log.

Questioner API is the project's API and provides functionality to the front end.

The project is managed on a pivotal tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2235290)



Features
----------------
1. Admin can create meetups
2. Users can view a specific meetup details
3. Users can RSVP a meetup
4. User can post a question to a specific meetup
5. Users can upvote or downvote a question
6. Users can view upcoming meetups



### Available Endpoints:

| Http Method | Endpoint Route                         | Endpoint Functionality      |
| :---------- | :------------------------------------- | :-------------------------- |
| POST        | /api/v1/meetups                        | Creates a meetup            |
| GET         | /api/v1/meetups                        | Gets all meetups            |
| GET         | /api/v1/meetups/meetup_id              | Gets a meetup by id         |
| GET         | /api/v1/meetups/upcoming               | gets upcoming meetups       |
| DELETE      | /api/v1/meetups/meetup_id              | Deletes a meetup            |
| POST        | /api/v1/meetups/meetup_id/rsvps        | Creates an RSVP to a meetup |
| POST        | /api/v1/questions                      | Creates a new question      |
| GET         | /api/v1/questions                      | Gets all questions          |
| GET         | /api/v1/questions/question_id          | Gets a question by id       |
| DELETE      | /api/v1/questions/question_id          | Deletes a question          |
| PATCH       | /api/v1/questions/question_id/upvote   | Upvotes a question          |
| PATCH       | /api/v1/questions/question_id/downvote | Downvotes a question        |



Pre-requisites
-------------
- Postman
- Git
- Python
- flask

Testing
----------------
- Clone this repository to your computer
    ```
    git clone https://github.com/mr-pagani/ADC-Questioner-API.git
    ```

- cd into this folder:
    ```
    ADC-Questioner-API
    ```

- From the terminal execute run.py

- Test the endpoints with Postman[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/52a74d96a869744dedfe)

Authors
----------------
**Brian Mwai** - _Initial work_ [mr-pagani](https://github.com/mr-pagani)

License
----------
This project is licensed under the The Unlicense. See [LICENSE](https://github.com/mr-pagani/ADC-Questioner/blob/master/LICENSE) for details.

Contribution
---------------
Fork this repository, contribute, and create a pull request to this repository's develop branch.
