import http.client
import json
conn = http.client.HTTPSConnection("https://www.pddapi.com")
payload = json.dumps({
   "xxx": "xxx",
})
headers = {
   'Nice-Apikey': 'xxx',
   'Content-Type': 'application/json'
}
conn.request("GET", "/api/v1/apiboxes/send_api/ksdy", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
