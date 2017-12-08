
import json
import requests
import sys


class KahootScraper:

    url = "https://create.kahoot.it/rest/authenticate"
    # Dictionary with login data
    authparams = {"username": 'YOUR USERNAME HERE',
                  "password": 'YOUR PASSWORD HERE',
                  "grant_type": "password"}
    try:
        r = requests.post(url, data=json.dumps(authparams),
                          headers={"content-type": "application/json"})
    except requests.ConnectionError as e:
        sys.exit(1)
    r.raise_for_status()

    token = r.json()[u"access_token"]


    def getAnswers(self, game_id):

        url = "https://create.kahoot.it/rest/kahoots/" + game_id

        r = requests.get(url, headers={
        "content-type": "application/json",
        "authorization": self.token})

        answers = []

        r.raise_for_status()

        raw_output = r.json()[u"questions"]

        print (raw_output)

        for question in raw_output:
            for index, choice in enumerate(question['choices']):
                if choice['correct'] == True:
                    #print(question['question'] + choice['answer'])

                    answers.append(index)
        else:
            return(answers)

    def getQuestions(self, game_id):

        url = "https://create.kahoot.it/rest/kahoots/" + game_id

        r = requests.get(url, headers={
        "content-type": "application/json",
        "authorization": self.token})

        answers = []

        r.raise_for_status()
        colors = ["red", "blue", "yellow", "green"]
        raw_output = r.json()[u"questions"]

        print (raw_output)

        for question in raw_output:
            for index, choice in enumerate(question['choices']):
                if choice['correct'] == True:
                    #print()

                    answers.append(question['question'] + ": Answer: " + choice['answer'] + " (" + colors[index] + ") ")
        else:
            return(answers)


    def getTimes(self, game_id):

        url = "https://create.kahoot.it/rest/kahoots/" + game_id

        r = requests.get(url, headers={
                "content-type": "application/json",
                "authorization": self.token})

        times = []

        r.raise_for_status()

        raw_output = r.json()[u"questions"]


        for question in raw_output:
            for index, choice in enumerate(question['choices']):
                times.append(question['time'])

        return times






