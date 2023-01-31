import requests, base64, os, json

image_path = os.path.join(os.getcwd(),'0.png') # "sample_image.png"
with open(image_path, "rb") as image_file:
    binary_image = image_file.read()
    base64_image = base64.b64encode(binary_image).decode('utf-8')

api_url = "http://localhost:5000"

json_data={ "image" : base64_image}
r= requests.post(api_url, json=json_data)
resp_dict = json.loads(r.text)
print(resp_dict)