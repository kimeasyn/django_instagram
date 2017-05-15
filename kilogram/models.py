from django.db import models
from django.conf import settings
# Create your models here.

def user_path(instance, filename):  #instance = Photo 모델의 변수이름, filename = 업로드한 사진 파일명
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return "%s%s.%s" % (instance.owner.username, pid, extension)


class Photo(models.Model):
    image = models.ImageField(upload_to = user_path)
    #pip install pillow 필요
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    thumnail_image = models.ImageField(blank = True)
    comment = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add = True)
