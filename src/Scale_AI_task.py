import scaleapi
import requests
import json
from pathlib import Path

script_dir = Path(__file__).parent
csv_file_path = script_dir.parent / "data" / "tasks.csv"
API_KEY = 'live_027cb75ff7cc4a67a940be914b993972'
client = scaleapi.ScaleClient(API_KEY)
taskId = "5f127f6f26831d0010e985e5"

# Downloads all completed tasks from a project and saves them to a jsonl file
url = f"https://api.scale.com/v1/task/{taskId}"

headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.request("GET", url, headers=headers)

print(response.text)

