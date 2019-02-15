import requests
import json

json_obj = {
"key":"value"
}
url = "https://raw.githubusercontent.com/inwk6312winter2019/openbookfinal-wesjone/master/access.log"

# need to specify content type -json- for POST request #
headers = {'content-type': 'application/json'}
response = requests.post(url, json.dumps(json_obj), headers=headers,verify=False)
response = requests.get(url,verify=False)

