from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, "homepage.html")
def menu(request):
    return render(request, "menu.html")
def chi_siamo(request):
    return render(request, 'chi_siamo.html')
def variabili(request):
    contex = {'var1':'1', 'var2':'2', 'var3':'3'}
    return render(request, 'variabili.html', contex)
def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'num_visits': num_visits}
    return render(request, "index.html", context)