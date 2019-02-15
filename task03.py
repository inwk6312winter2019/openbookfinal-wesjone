import requests
def getTickets():
  import json
  url = 'http://developer.cisco.com/sandbox/apic_em/api/v1/ticket'
  payload ={'username':'developuser','password':'cisco123':} 
  headers = {'congtent-type':'application/json'}
  response = requests.get(url,verify=False)

getTickets()

