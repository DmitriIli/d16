from django.shortcuts import render
from board.settings import BASE_DIR

# Create your views here.


def mainview(request):
    context={}
    return render(request,template_name='default.html',context=context)