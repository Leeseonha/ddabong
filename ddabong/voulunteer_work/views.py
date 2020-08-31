from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Works

#############봉사 등록  Works###########################  
def WorksForm(request, works = None):
    if request.method == 'POST':
        form = WorksForm(request.POST, instance = works)
        if form.is_valid():
            works = form.save(commit = True)
            works.v_name = request.GET['v_name']
            works.pub_date = timezone.datetime.now()
            works.v_member = request.GET['v_member']
            works.body = request.GET['body']
            works.save()
            return redirect('/theme/v_all/')
    else:
        form = WorksForm(instance = works)
        return render(request,'theme/index.html',{'form':form})

################봉사 나열 V_all###########################

def v_all(request):
    works = Works.objects
    return render(request, 'v_all.html', {'works':works})


####################봉사 상세#################################

def v_detail(request):
    return render(request, 'v_detail.html')

##############내주변 봉사###############
def v_area(request):
    return render(request, 'v_area.html')