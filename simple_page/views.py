from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})