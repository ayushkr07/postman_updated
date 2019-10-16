from django.urls import path
from . import views

urlpatterns = [
    path('api/upload', views.upload_to_s3,name="upload_to_s3"),
    path('api/getpath/<str:pathurl>',views.get_file_path,name="get_file_path")

]