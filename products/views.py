from django.shortcuts import render

# Create your views here.

def home(request):
    if request.user.is_authenticated():
        username_is = "Raja is using Context"
        context = {"username_is": request.user}
    else:
        context = {"username_is": request.user}
    template = 'products/home.html'
    return render(request, template, context)