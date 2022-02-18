import os
import requests
from flask import Flask, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

app = Flask(__name__)

bolt_app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@bolt_app.event("app_home_opened")
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
              "text": "Still works  New Paid Time Off request from <example.com|Fred Enriquez>\n\n<https://example.com|View request>"
            }
          }
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")



handler = SlackRequestHandler(bolt_app)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    """ Declaring the route where slack will post a request and dispatch method of App """
    return handler.handle(request)


@app.route("/hello", methods=["POST"])
def hello():
  url = 'https://slack.com/api/chat.postMessage'
  headers = {'Authorization': 'Bearer xoxb-3104380765749-3122787789140-dIIc9gXtvzz7cdiJeUaRx16V'}
  payload = {
    'channel': 'C03486V8XKJ',
    'text': 'from the api'
  }

  r =requests.post(url, headers=headers, data=payload)
  print(r.text)
  return "good"




# Start your app
if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 3000)))