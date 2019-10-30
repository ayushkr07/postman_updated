from django.test import SimpleTestCase
from django.urls import reverse,resolve
from filehandling.views import upload_to_s3,get_file_path

class TestUrls(SimpleTestCase):

    def test_upload_to_s3(self):
        url=reverse('upload_to_s3')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,upload_to_s3)

    def test_get_file_path(self):
        url=reverse('get_file_path',args=['pathurl'])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,get_file_path)

    def test_get_file_no_path(self):
        url=reverse('get_file_paths')
        #print(resolve(url))
        self.assertEquals(resolve(url).func, get_file_path)