import json
import requests
from pprint import pprint

url = "https://api.carlisleny.com/zs7/toolkit/planning_sheet.php"

payload = json.dumps(
    {"company_start": "ccstart", "account": "00718", "season": "C"})

response = requests.post(url, data=payload)

pprint(response.content)
