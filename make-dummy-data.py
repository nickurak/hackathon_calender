#!/usr/bin/env python3

import json

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


def main():
    with open("calendars.json", "w") as outfile:
        json.dump(sample_registered_calendars, outfile)
        outfile.write("\n")

    with open("events.json", "w") as outfile:
        json.dump(sample_events, outfile)
        outfile.write("\n")

if __name__ == '__main__':
    main()
