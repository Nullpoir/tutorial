from django.shortcuts import render

# Create your views here.

def TopPageView(requests):
    return render(requests,"index.html")
