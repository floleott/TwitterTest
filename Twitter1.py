#load the credentials from a local file
import json
with open(credentials.json) as cr:
    data = json.load(cr)

print data
