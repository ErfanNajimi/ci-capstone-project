from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def public(request):
    return render(
        request,
        "public/index.html",
    )