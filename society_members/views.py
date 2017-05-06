from django.http import HttpResponse
def index(request):
    return HttpResponse("<p>This is society members app</p>")