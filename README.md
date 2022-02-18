# chris slack server

Code for the web server server that the *Chris Demo App* slack app will use.

This tutorial was used to get me started:
[https://api.slack.com/start/building/bolt-python](https://api.slack.com/start/building/bolt-python)

The tutorial mentioned above explains how to start this server and setup your slack app to use it.

## Modifications

I wanted to be able to include my own endpoints along with the handlers for /slack/events endpoint calls.

I saw an article that gave me some understanding about how this could be done:
[https://python.plainenglish.io/lets-create-a-slackbot-cause-why-not-2972474bf5c1](https://python.plainenglish.io/lets-create-a-slackbot-cause-why-not-2972474bf5c1)

## Questions

Feel to contact me (Chris) in our slack team channel **#ddm-hackathon-universal-calendar** about any questions or any issues you encounter following tutorial linked above.

# Development environment:

Python supports "Virtual Enverionments" that keep all the dependencies we install isolated from anything else on your computer.

There's a helper script to run this. Just run:

. activate-virtualenv

Then, anything else you install with the python package manager "pip" will be kept in this folder, and only available when this virtual environment is active.
