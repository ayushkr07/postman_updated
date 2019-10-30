import unittest
from django.test import Client
from django.urls import reverse
import json

from moto import mock_s3
from boto3.session import Session

from filehandling.views import *


class S3TestCase(unittest.TestCase):

    def setUp(self):
        session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_S3_REGION_NAME)
        s3 = session.resource('s3')
        s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key='style.css', Body='value')

        self.client=Client()
        self.get_file_path_url=reverse('get_file_Path',args=['style.css'])
        self.get_file_path_no_url = reverse('get_file_Paths')

    @mock_s3
    def test_get_file_no_path(self):
        response = self.client.get(self.get_file_path_no_url)
        self.assertEquals(response.status_code, 200)


    @mock_s3
    def test_get_file_path(self):
        response=self.client.get(self.get_file_path_url)
        self.assertEquals(response.status_code,200)

