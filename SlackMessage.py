import requests
import sys
import getopt

#slack api
def send_slack_msg(message):
  payload = '{"text": "%s"}' % message
  response = requests.post('https://hooks.slack.com/services/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',
  data = payload)
  print(response.text)
def main(argv):

  message = ''

  try: opts, args = getopt.getopt(argv,"hm:", ["message="])

  except getopt.GetoptError:
    print('SlackMessage.py -m <message>')
    sys.exit(2)
  if len(opts) == 0:
    message = "SlackMessage"
  for opt, arg in opts:
    if opt == '-h':
      print('SlackMessage.py -m <message>')
      sys.exit(2)
    elif opt in ("-m", "--message"):
      message = arg
  
  send_slack_msg(message)

if __name__ == "__main__":
  main(sys.argv[1:])