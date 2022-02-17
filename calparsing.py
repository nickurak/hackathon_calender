import requests
from icalendar import Calendar, Event
from db import get_calendars, write_events
from datetime import timezone

events = []
for calendar in get_calendars():
        name = calendar['name']
        url = calendar['url']

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
          
        write_events(events)