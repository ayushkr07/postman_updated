from django.http import JsonResponse, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

import boto3
from cloudstorage.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
from boto3.session import Session

session = Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            region_name=AWS_S3_REGION_NAME)
s3 = session.resource('s3')



def upload_to_s3(request):
    if request.method == 'POST':
        try:
            uploaded_file= request.FILES['documents']
        except MultiValueDictKeyError:
            return JsonResponse({'status': 'failed', 'message': 'file is null,Add file '}, safe=False)
        s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(Key=uploaded_file.name,Body=uploaded_file)
        return JsonResponse({'status': 'success', 'message': 'file has been uploaded'}, safe=False)

def get_file_path(request,pathurl=None):
    if request.method == 'GET':
        if pathurl is None:
            return JsonResponse({'status': 'failed', 'message':"File Name not in URL"}, safe=False)
        bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
        for object in bucket.objects.all():
            if object.key == pathurl:
                url = "https://%s.%s.amazonaws.com/%s" % (AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, pathurl)
                return JsonResponse({'status': 'success', 'message': url}, safe=False)
        return JsonResponse({'status': 'failed', 'message':"File Not Exists"}, safe=False)



