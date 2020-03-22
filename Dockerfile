FROM python:3.8-slim
#RUN apt-get update
#RUN apt-get install -y python3-pip
#RUN apt-get install gifsicle
COPY . /Module1_VideoPreprocessing
WORKDIR /Module1_VideoPreprocessing
RUN pip install -r requirements.txt
CMD ["python", "run.py"]