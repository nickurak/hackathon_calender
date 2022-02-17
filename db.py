import json

def get_events():
    with open("events.json", "r") as event_file:
        events = json.load(event_file)
        for event in events:
            uid = event['uid']
            name = event['event_name']
            start_time = event['start_time'],
            end_time = event['end_time'],
            calendar = event['calendar']
            yield {
                'uid': uid,
                'calendar': calendar,
                'event_name': name,
                'start_time': event['start_time'],
                'end_time': event['end_time'],
            }

def get_calendars():
    with open("calendars.json", "r") as cal_file:
        data = json.load(cal_file)
        for calendar in data:
            name = calendar['name']
            url = calendar['url']
            yield {
                'name': name,
                'url': url
            }

