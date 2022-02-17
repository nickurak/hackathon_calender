#!/usr/bin/env python3

from datetime import datetime

from db import get_events, get_calendars

def main():
    for calendar in get_calendars():
        name = calendar['name']
        url = calendar['url']
        print(f"Calendar '{calendar}' is at url '{url}'")

    for event in get_events():
        uid = event['uid']
        name = event['event_name']
        start_time = datetime.utcfromtimestamp(event['start_time'])
        end_time = datetime.utcfromtimestamp(event['end_time'])
        calendar = event['calendar']
        print(f"Event {name} from calendar {calendar} (with uid \"{uid}\" ), starts at {start_time} and goes until {end_time}")

if __name__ == '__main__':
    main()