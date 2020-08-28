from django.db import models

# Create your models here.
class works(models.Model):
    v_name = models.CharField(max_length = 200) #봉사이름
    pub_date = models.DateTimeField('date published') #게시글 날짜
    v_organ = models.CharField(max_length = 200, blank= True) #봉사기관 이름 (빈칸 허용)
    # v_date #모집 날짜
    v_member = models.IntegerField(default=True) # 모집 인원 수   
    v_finish = models.BooleanField(default=True) # 모집 끝났는지 여부
    v_point = models.IntegerField(default=True) # 제공 포인트
    body = models.TextField() #내용
