import os
import requests
from datetime import datetime
from slack_bolt import App
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": f"Time is {datetime.now().strftime('%H:%M:%S')}. Still works  New Paid Time Off request from <example.com|Fred Enriquez>\n\n<https://example.com|View request>"
            }
          }
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")



# helpers
def sayHello():
  url = 'https://slack.com/api/chat.postMessage'
  headers = {'Authorization': f'Bearer {os.environ.get("SLACK_BOT_TOKEN")}'}
  payload = {
    'channel': 'C03486V8XKJ',
    'text': f'from the api at {datetime.now().strftime("%H:%M:%S")}'
  }
  
  r =requests.post(url, headers=headers, data=payload)
  # print(r.text)



# internal "cron job" setup
from threading import Thread
import threading

event = threading.Event()
class cron(Thread):
  def run(self):
    while True:
      sayHello()
      event.wait(1)



# Start your app
if __name__ == "__main__":
  cron().start()
  app.start(port=int(os.environ.get("PORT", 3000)))    