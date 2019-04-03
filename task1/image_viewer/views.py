from django.shortcuts import render
from django.http import HttpResponse , Http404

from .models import Images
from django.forms import modelformset_factory


# Create your views here.
def home_view(request,*args,**kwargs):
    user=request.user
    context ={
    'user':user
    }
    return render(request,'image_viewer/home.html',context)

def image_viewer_view(request):
    obj = Images.get(all)
    
