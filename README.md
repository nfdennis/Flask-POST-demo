# Flask App to output/return readable schedule
### get:
- returns {} or previously posted JSON object

### post:
- outputs to server console a readable schedule
- returns {schedule: str({readableSchedule})

## Workspace setup
copy requirements.txt
pip install

## Run in debug

python3 main.py 

get:
curl --request GET http://127.0.0.1:5000/schedule

post:
curl --header "Content-Type: application/json" --request POST --data '{ "monday":[ ], "tuesday":[ { "title": "Meet with John", "start":"36000", "end":"39600" }, { "title":"Dentist", "start":57600, "end":"61200" } ], "wednesday":[ ], "thursday":[ { "title":"Paper Writing", "start":36000,"end":"46800" }, { "title":"Meet with Boss", "start":39600,"end":"43200" } ], "saturday":[ { "title":"Farmers Market", "start":36000,"end":"41400" } ], "sunday":[ ], "friday":[ { "title":"Update AWS", "start":50400 ,"end":52200} ,{"title":"pick up kids from school","start":"54000", "end":"55800"}]} ' http://127.0.0.1:5000/schedule