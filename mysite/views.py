from django.http import HttpResponse

def index(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('About Page')

def navigator(request):
    return HttpResponse('''
        <h1>Personal Navigator</h1><br>
        <span><a href="www.google.com" target="_blank">Goolge</a></span><br>
        <span><a href="https://github.com/Barun355" target="_blank">Github</a></span><br>
        <span><a href="https://stackoverflow.com/users/19755163/barun-tiwary-21me60" target="_blank">StackOverflow</a></span><br>
    ''')