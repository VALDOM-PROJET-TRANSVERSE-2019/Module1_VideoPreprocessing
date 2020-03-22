"""
Module for testing flask api with unittest
"""
import os
import shutil
import unittest
import urllib
from urllib import request
from urllib.error import HTTPError

import cv2
import numpy as np


class TestGet(unittest.TestCase):
    """
    Test class for unittest
    """
    data = {'Video_path': 'data/car.flv', "Output_path": 'data/', 'Sampling': 1}
    data_video_path_missing = {"Output_path": 'data/'}
    data_output_path_missing = {'Video_path': 'data/car.flv'}
    data_all_missing = {}

    def test_output_type(self):
        """
        Test types of output request
        Test values and length of output request
        :return:
        """
        url_values = urllib.parse.urlencode(self.data)
        url = "http://0.0.0.0:5001/Image%20processing/"
        full_url = url + '?' + url_values

        req = request.Request(full_url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')

        request.urlopen(full_url).read()
        fold = [path for path, dirs, files in os.walk(self.data["Output_path"])][1:]
        img = cv2.imread(fold[0] + "/image11.jpg", cv2.IMREAD_GRAYSCALE)
        self.assertEqual(type(img).__module__, np.__name__)

        shutil.rmtree(fold[0])

    def test_video_sampling_parameter(self):
        """
        Tests video sampling parameter
        :return:
        """
        data = {'Video_path': 'data/car.flv', "Output_path": 'data/', 'Sampling': 1}
        data2 = {'Video_path': 'data/car.flv', "Output_path": 'data/', 'Sampling': 3}

        url_values = urllib.parse.urlencode(data)
        url = "http://0.0.0.0:5001/Image%20processing/"
        full_url = url + '?' + url_values

        req = request.Request(full_url)
        request.urlopen(req).read()

        url_values = urllib.parse.urlencode(data2)
        url = "http://0.0.0.0:5001/Image%20processing/"
        full_url = url + '?' + url_values

        req = request.Request(full_url)
        request.urlopen(req).read()
        folder = [path for path, dirs, files in os.walk(data["Output_path"])][1:]

        self.assertEqual(len(os.listdir(folder[0])) / 3,
                         len(os.listdir(folder[1])))
        for fol in folder:
            shutil.rmtree(fol)

    def test_video_path_missing(self):
        """
        Tests error message values when video_path is missing
        :return:
        """
        url_values = urllib.parse.urlencode(self.data_video_path_missing)
        url = "http://0.0.0.0:5001/Image%20processing/"
        full_url = url + '?' + url_values

        req = request.Request(full_url)
        with self.assertRaises(HTTPError):
            request.urlopen(req).read()

    def test_output_path_missing(self):
        """
        Tests error message values when Output_path is missing
        :return:
        """
        url_values = urllib.parse.urlencode(self.data_output_path_missing)
        url = "http://0.0.0.0:5001/Image%20processing/"
        full_url = url + '?' + url_values

        req = request.Request(full_url)
        with self.assertRaises(HTTPError):
            request.urlopen(req).read()

    def test_error_all_missing(self):
        """
        Tests error message values when all parameters are missing
        :return:
        """
        url_values = urllib.parse.urlencode(self.data_all_missing)
        url = "http://0.0.0.0:5001/Image%20processing/"
        full_url = url + '?' + url_values

        req = request.Request(full_url)
        with self.assertRaises(HTTPError):
            request.urlopen(req).read()
