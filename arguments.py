import sys
from datetime import datetime
from time import time

global file_name
# global action

def read_log():
  """Reads from the log file"""
  with open(file_name, r) as log_messages:
    print(log_messages.read())


def log(message, action):
  """Log a message to the log file

  Argments:
    message -- Any string
  """
  with open(file_name, action) as logger:
    timestamp = time()
    logger.write("{0}: {1}
".format(
      datetime.fromtimestamp(timestamp).strftime(%Y-%m-%d %H:%M:%S),
      str(message)
    ))


if __name__ == "__main__":
  try:
    file_name = sys.argv[1]
    action = sys.argv[2]

    if action == r:
      read_log()
    elif action == w or action == a:
      log( .join(sys.argv[3:]), action)
  except IndexError:
    pass







