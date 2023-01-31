FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip 
RUN apt-get update

RUN apt-get install -y python3 python3-pip ffmpeg libsm6 libxext6 libgl1-mesa-dev

RUN python3 -m pip install -r requirements.txt

#CMD uvicorn app_fastapi:app 
#--reload
CMD ["python","./app.py"]

# docker build -t mnist_digit_recognition .
# docker push mnist_digit_recognition
# docker run -p 5000:5000 -td mnist_digit_recognition