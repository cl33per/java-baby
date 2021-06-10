import requests

r= requests.get('https://fedramp.mod.udpaas.com/API/1/user/?companyid=1541170&apitoken=BGBzdQVGcnA1R3JUblVCXAVkfV0BaXcECzEPCQ~~&alias=fedramp&username=udpaas_api_user@etranservices.com&password=1234567890')
r.status_code
r.headers
r.text
print (r.json())
