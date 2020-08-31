from django.db import models

#봉사등록
class Works(models.Model):
    v_name = models.CharField(max_length = 200) #봉사이름
    pub_date = models.DateTimeField('date published') #게시글 날짜
  #이거 두개 왜 오류나는지...# v_organ = models.CharField(max_length = 200, blank= True) #봉사기관 이름 (빈칸 허용)
    #v_date = v_organ = models.CharField(max_length = 200, blank= True) #모집 날짜 *****바꿔야됨
    v_member = models.IntegerField(default=True) # 모집 인원 수   
  #이건 등록시 필요없음, 나중에 나열될때  v_finish = models.BooleanField(default=True) # 모집 끝났는지 여부
    v_point = models.IntegerField(default=True) # 제공 포인트
    body = models.TextField() #내용

    class Meta:
        managed = False
        db_table = 'v_lists'
