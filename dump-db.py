#!/usr/bin/env python3

import json
from datetime import datetime

timestamp = datetime.fromtimestamp(1500000000)
print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))

def main():
    with open("calendars.json", "r") as cal_file:
        data = json.load(cal_file)
        for calendar in data:
            name = calendar['name']
            url = calendar['url']
            print(f"Calendar '{calendar}' is at url '{url}'")

    with open("events.json", "r") as event_file:
        events = json.load(event_file)
        for event in events:
            uid = event['uid']
            name = event['event_name']
            start_time = datetime.utcfromtimestamp(event['start_time'])
            end_time = datetime.utcfromtimestamp(event['end_time'])
            calendar = event['calendar']
            print(f"Event {name} from calendar {calendar} (with uid \"{uid}\" ), starts at {start_time} and goes until {end_time}")

if __name__ == '__main__':
    main()
