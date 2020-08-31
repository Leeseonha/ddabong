from django.shortcuts import render, redirect
from django.views.generic. base import TemplateView

# Create your views here.
def MainpageView(request):
    # template_name = 'index.html'
    # code = request.GET['code']
    # print('code= ' + str(code))
    return render(request,'index.html',)