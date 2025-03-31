import scaleapi
import requests
import json
from pathlib import Path
import pandas as pd
from PIL import Image
from io import BytesIO

script_dir = Path(__file__).parent
csv_file_path = script_dir.parent / "data" / "tasks.csv"
API_KEY = 'live_027cb75ff7cc4a67a940be914b993972'
client = scaleapi.ScaleClient(API_KEY)



taskId = "5f127f6f26831d0010e985e5"

## Have the task response. Can also get the image from th response. Will find out height and width of image for comparison with boxes
## Non Visible faces should be small and not bigger than a certain amount 


# Downloads all completed tasks from a project and saves them to a jsonl file
url = f"https://api.scale.com/v1/task/{taskId}"

headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.request("GET", url, headers=headers)

image_url = response.json()["params"]["attachment"] 

def get_image_dimensions(url):
    try:
        headers = {"Range": "bytes=0-1023"}  
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        return img.size  # (width, height)
    except Exception as e:
        print(f"Error fetching image from {url}: {e}")
        return None

im_dim = get_image_dimensions(image_url)

print(im_dim)
print(image_url)
# print(response.text)

###Checks for the responses




