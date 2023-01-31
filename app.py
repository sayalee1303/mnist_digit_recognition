from flask import Flask,request, jsonify
#import os
from main import detection
import base64
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():

  if request.method == 'POST':
    data = request.get_json(force=True)
    content=data['image']

    if ";base64," in content:
        data=content.split(";base64,")[1].encode("utf8")
    else:
        data=content.encode("utf8")

    image_path='input.png'
    with open(image_path, "wb") as fp:
        fp.write(base64.decodebytes(data))

    digit= detection(image_path)

  return jsonify({'Digit': str(digit)})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)