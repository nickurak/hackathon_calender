import os
import requests
from datetime import datetime
import json

from calparsing import read_allcalendars

from periodic import periodic

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


                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Add a new channel subscription",
                            "emoji": True
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "channels_select",
                                "placeholder": {
                                    "type": "plain_text",
                                    "text": "Select a channel",
                                    "emoji": True
                                },
                                "action_id": "actionId-1"
                            },
                            {
                                "type": "static_select",
                                "placeholder": {
                                    "type": "plain_text",
                                        "text": "Select an calendar",
                                        "emoji": True
                                },
                                "options": [
                                    {
                                        "text": {
                                            "type": "plain_text",
                                            "text": "Registered Calendar 1*",
                                            "emoji": True
                                        },
                                        "value": "value-0"
                                    },
                                    {
                                        "text": {
                                            "type": "plain_text",
                                            "text": "Registered Calendar 2",
                                            "emoji": True
                                        },
                                        "value": "value-1"
                                    },
                                    {
                                        "text": {
                                            "type": "plain_text",
                                            "text": "Registered Calendar 3",
                                            "emoji": True
                                        },
                                        "value": "value-2"
                                    }
                                ],
                                "action_id": "actionId-3"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                                "text": "Your schedule will arrive Monday - Friday at 8:00 am in your current time zone",
                                "type": "mrkdwn"
                        },
                        "accessory": {
                            "type": "button",
                            "action_id": "change_delivery_time",
                            "text": {
                                    "text": "Change delivery time",
                                    "type": "plain_text"
                            }
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                                "type": "mrkdwn",
                                "text": "Save settings:"
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                    "type": "plain_text",
                                    "text": "Add",
                                    "emoji": True
                            },
                            "value": "click_me_123",
                            "action_id": "button-action"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "header",
                        "text": {
                                "type": "plain_text",
                                "text": "Existing reminders",
                                "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                                "text": "#channelA <calendar 1 name> Monday - Friday at 8:00 am",
                                "type": "mrkdwn"
                        },
                        "accessory": {
                            "type": "button",
                            "action_id": "change_delivery_time",
                            "text": {
                                    "text": "Delete",
                                    "type": "plain_text"
                            }
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                                "text": "#channelA <calendar 1 name> Monday - Friday at 8:00 am",
                                "type": "mrkdwn"
                        },
                        "accessory": {
                            "type": "button",
                            "action_id": "change_delivery_time",
                            "text": {
                                    "text": "Delete",
                                    "type": "plain_text"
                            }
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "header",
                        "text": {
                                "type": "plain_text",
                                "text": "Add a new calendar",
                                "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "element": {
                                "type": "plain_text_input",
                                "action_id": "new_calendar_name_action"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Name your calendar",
                            "emoji": False
                        }
                    },
                    {
                        "type": "input",
                        "element": {
                                "type": "plain_text_input",
                                "action_id": "new_calendar_url_action"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "URL",
                            "emoji": False
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                                "type": "mrkdwn",
                                "text": "Save settings:"
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                    "type": "plain_text",
                                    "text": "Add"
                            },
                            "value": "click_me_123",
                            "action_id": "button-action"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "header",
                        "text": {
                                "type": "plain_text",
                                "text": "Registered calendars"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                                "text": "Hackathon Calendar 1 `https://some-calendar-url/`",
                                "type": "mrkdwn"
                        },
                        "accessory": {
                            "type": "button",
                            "action_id": "delete_calendar_1",
                            "text": {
                                    "text": "Delete",
                                    "type": "plain_text"
                            }
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                                "text": "Hackathon Calendar 2 `https://some-other-calendar-url/`",
                                "type": "mrkdwn"
                        },
                        "accessory": {
                            "type": "button",
                            "action_id": "delete_calendar_2",
                            "text": {
                                    "text": "Delete",
                                    "type": "plain_text"
                            }
                        }
                    },
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
@periodic(5*60)
def say_hello():
  url = 'https://slack.com/api/chat.postMessage'
  headers = {'Authorization': f'Bearer {os.environ.get("SLACK_BOT_TOKEN")}'}
  blocks = [
      {
	  "type": "section",
	  "text": {
	      "type": "mrkdwn",
	      "text": "*<Event Description>*\n<start_time>-<end_time>" + f'\nCurrent time:  {datetime.now().strftime("%H:%M:%S")}'
	  },
	  "accessory": {
	      "type": "button",
	      "action_id": "event_1_reminder",
	      "text": {
		  "text": "Learn More",
		  "type": "plain_text"
	      }
	  }
      }
  ]

  payload = {
    'channel': 'C03486V8XKJ',
    'blocks': json.dumps(blocks)
  }
  
  r =requests.post(url, headers=headers, data=payload)
  # print(r.text)

@periodic(10*60)
def refresh_calendars():
    read_allcalendars()

# internal "cron job" setup
from threading import Thread
import threading

event = threading.Event()
class cron(Thread):
  def run(self):
    while True:
      say_hello()
      refresh_calendars()

      event.wait(1)



# Start your app
if __name__ == "__main__":
  cron().start()
  app.start(port=int(os.environ.get("PORT", 3000)))    
