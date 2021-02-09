from django.shortcuts import render

# Create your views here.
'''
def index(request):
    return render(request,'index.html')
'''
from django.views import generic
class IndexView(generic.ListView):
    model=model1