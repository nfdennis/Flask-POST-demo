from flask import Flask, request
from flask_restx import Resource, Api, reqparse
from collections import OrderedDict
import datetime

app = Flask(__name__)
api = Api(app)

orderedSchedule = OrderedDict()

# convert seconds to datetime
def convertTime(n):
    return str(datetime.timedelta(seconds = n))

# print readable schedule
def createReadableString(input):
    printOut = ''
    conflict = False
    prevStart = 0
    prevEnd = 0
    for key, values in input.items():
        if not values:
            printOut += (key + ': ' + 'No appointments ' + '\n')
        if(isinstance(values, list)):
            sortedEvents = sorted(values, key=lambda event: str(event['start']))
            for value in sortedEvents:
                if int(value['start']) > prevStart and int(value['start']) < prevEnd:
                    conflict = True
                prevStart = int(value['start'])
                prevEnd = int(value['end'])
                title = value['title']
                start = convertTime(int(value['start']))
                end = convertTime(int(value['end']))
                printOut += key + ': ' + title + ' ' + start + ' - ' + end + '\n'
    if conflict is True: 
        printOut += 'Conflicts?: Yes'
    return printOut


@api.route('/schedule')
class Schedule(Resource):
    def get(self):
        return {'Schedule': orderedSchedule}

    # creates ordered week dict from data monday through sunday
    def post(self):
        if request.get_json() is not None:
            orderedSchedule["Monday"] = request.get_json().get("monday")
            orderedSchedule["Tuesday"] = request.get_json().get("tuesday")
            orderedSchedule["Wednesday"] = request.get_json().get("wednesday")
            orderedSchedule["Thursday"] = request.get_json().get("thursday")
            orderedSchedule["Friday"] = request.get_json().get("friday")
            orderedSchedule["Saturday"] = request.get_json().get("saturday")
            orderedSchedule["Sunday"] = request.get_json().get("sunday")

        ret = createReadableString(orderedSchedule)
        print(ret)
        return str(ret)
        

if __name__ == "__main__":
    app.run(debug=True)