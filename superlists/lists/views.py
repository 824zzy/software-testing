from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homePage(request):
    # render: automatically search `templates` folders and builds an HttpResponse.
    return render(request, 'home.html')