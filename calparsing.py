import requests
from icalendar import Calendar, Event

URL = "https://calendar.google.com/calendar/ical/c_adghr2e0nnjq9ve4a408lh8dc4%40group.calendar.google.com/public/basic.ics"

r = requests.get(url = URL)

print ("Status Code:", r.status_code)

gcal = Calendar.from_ical(r.text)

for component in gcal.walk():
  if component.name == "VEVENT":
        print("Summary:",component.get('summary'))
        print("Date Start:",component.get('dtstart').dt)
        print("Date End:",component.get('dtend').dt)
        print("Date Stamp:",component.get('dtstamp').dt)
