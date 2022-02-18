import requests
from icalendar import Calendar, Event
from db import get_calendars, write_events
from datetime import timezone

def read_calender_events(calendar, events):
    r = requests.get(url = calendar['url'])

    gcal = Calendar.from_ical(r.text)

    for component in gcal.walk():
        if component.name == "VEVENT":
            event = {}
            event['calendar'] = calendar['name']
            event['event_name'] = component.get('summary')
            event['uid'] = component.get('uid')
            event['start_time'] = component.get('dtstart').dt.replace(tzinfo=timezone.utc).timestamp()
            event['end_time'] = component.get('dtend').dt.replace(tzinfo=timezone.utc).timestamp()
            events.append(event)


def read_allcalendars():
    events = []
    for calendar in get_calendars():
        read_calender_events(calendar, events)

    write_events(events)

def read_calendar(cname):
    for calendar in get_calendars():
        if cname == calendar['name']:
            read_calender_events(calendar)

    write_events(events)


def main():
    read_allcalendars()

if __name__ == '__main__':
    main()
