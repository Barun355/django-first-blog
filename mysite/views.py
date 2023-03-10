from django.http import HttpResponse

def index(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('About Page')