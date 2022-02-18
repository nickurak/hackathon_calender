import os
# Use the package we installed
from slack_bolt import App
from db import  write_reminders, get_reminders

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here
# @app.event("app_home_opened") etc

sample_reminders = [
    {
        'channel': '#chris-app-test',
        'calendar': "hackathon test calendar",
        'time': "6:00 EST"
    }
]


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  write_reminders(sample_reminders)
  
  sections =[
    
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
  ]

   for reminder in get_reminders():
      sections.append(
                    {
                        "type": "section",
                        "text": {
                                "text": {reminder.channel},
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
                    }
      )
     
  sections.append(
                    {
                        "type": "divider"
                    }
  )
  sections.append(
                    {
                        "type": "header",
                        "text": {
                                "type": "plain_text",
                                "text": "Add a new calendar",
                                "emoji": True
                        }
                    }
  )
  sections.append(
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
                    }
  )
  sections.append(
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
                    }
  )
  sections.append(
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
                    }
  )
  sections.append(
                    {
                        "type": "divider"
                    }
  )
  sections.append(
                    {
                        "type": "header",
                        "text": {
                                "type": "plain_text",
                                "text": "Registered calendars"
                        }
                    }
  )
  sections.append(
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
                    }
  )
  sections.append(
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
                    }
  )
  
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
        # the user that opened your app's app home
        user_id=event["user"],
        # the view object that appears in the app home
        view={
            "type": "home",
            "callback_id": "home_view",


            "blocks": sections

        }
    )

  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))