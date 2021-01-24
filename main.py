from datetime import datetime
import requests
import sys
import time

'''
This is a script to grab HTML from a website and compare it to a previous state.

`python main.py debug` to run three quick loops
`python main.py` to run in infinite loop with waitTime (second) waits
'''

# this dictionary will be modified in-place by adding current/previous HTML states
sitesToMonitor = {
  'heb': {
    'url': 'https://vaccine.heb.com/'
  },
  'houstonEmergency': {
    'url': 'https://houstonemergency.org/covid-19-vaccines/'
  }
}

waitTime = 60 # seconds
debugCycles = 3

'''
diffSite - a helper function to do the diffing
args:
  site(string) - a key from sitesToMonitor
  siteProperties(dictionary) - a corresponding value from sitesToMonitor
'''
def diffSite(site, siteProperties):
  siteProperties['current'] = requests.get(siteProperties['url']).text

  log = '[' + str(datetime.now()) + ']: ' + site + ' - '

  if siteProperties['current'] == siteProperties.get('previous', ''):
    log += 'Same'
  else:
    log += 'Different'

  print(log)

  siteProperties['previous'] = siteProperties['current']

def main(loop):
  count = 0

  while loop or count < debugCycles:
    for site, siteProperties in sitesToMonitor.items():
      diffSite(site, siteProperties)

    if not loop:
      count += 1
    else:
      time.sleep(waitTime)

# run `python main.py debug` to loop only 3 times
if __name__ == '__main__':
  if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    main(False)
  else:
    main(True)
