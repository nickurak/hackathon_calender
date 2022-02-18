#!/usr/bin/env python3

import json

from db import write_calendars, write_events, write_reminders

sample_registered_calendars = [
    {
        'name': 'hackathon test calendar',
        'url': 'https://calendar.google.com/calendar/ical/c_adghr2e0nnjq9ve4a408lh8dc4%40group.calendar.google.com/public/basic.ics',
    }
]



sample_events = [
    {
        'uid': 'some fake uid',
        'calendar': 'hackathon test calendar',
        'event_name': 'test event',
        'start_time': 1645124381,
        'end_time': 1645124989
    }
]

sample_reminders = [
    {
        'channel': '#chris-app-test',
        'calendar': "hackathon test calendar",
        'time': "6:00 EST"
    }
]


def main():
    write_calendars(sample_registered_calendars)
    write_events(sample_events)
    write_reminders(sample_reminders)

if __name__ == '__main__':
    main()
