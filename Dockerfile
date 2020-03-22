FROM python:3.8-slim
#RUN apt-get update
#RUN apt-get install -y python3-pip
#RUN apt-get install gifsicle
COPY . /Module1_VideoPreprocessing
WORKDIR /Module1_VideoPreprocessing
RUN apt-get update
RUN apt-get -y install libglib2.0-0
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN pip install -r requirements.txt
CMD ["python", "run.py"]