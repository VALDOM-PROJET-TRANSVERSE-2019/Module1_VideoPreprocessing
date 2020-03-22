"""
Routes for Flask app
"""
import os

from flask import Flask
from flask_restplus import Api, Resource, reqparse
import cv2

APP = Flask(__name__)
APP.config.from_object('config')
API = Api(app=APP, version='1.0', title='Tracker API')
PROCESSOR = API.namespace('Image processing', description="Convert video to frame")


@PROCESSOR.route('/')
class Processor(Resource):
    """
    Resource class to generate Swagger for REST API
    """

    @PROCESSOR.doc(params={'Video_path': 'A path', 'Output_path': 'A path', 'Sampling': 'float'})
    def get(self):
        """
        GET method, request the video path, output path, and sampling parameters
        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument('Video_path', type=str,
                            required=True, help='Image saving path')
        parser.add_argument('Output_path', type=str,
                            required=True, help='Video path')
        parser.add_argument('Sampling', type=float,
                            required=False, default=0.5, help='Sampling parameter')
        args = parser.parse_args()
        videocap = cv2.VideoCapture("/home/pa/PycharmProjects/Module4_VehicleTracking/data/video/car.flv")

        sec, count = 0, 0
        frame_rate = args.Sampling  # it will capture image in each sampling second
        videocap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        has_frames, image = videocap.read()
        # Create the folder if it doesn't exist
        os.makedirs(args.Output_path + "/Output/", exist_ok=True)

        while has_frames:
            count = count + 1
            sec = sec + frame_rate
            sec = round(sec, 2)
            videocap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
            has_frames, image = videocap.read()
            print(args.Output_path + "Output/" + "image" + str(count) + ".jpg")
            if has_frames:
                cv2.imwrite(args.Output_path + "/Output/" + "image" + str(count) + ".jpg",
                            image)  # save frame as JPG file

        # return the new frames collection id
        return "frames collection id! " + str(args.Video_path)
