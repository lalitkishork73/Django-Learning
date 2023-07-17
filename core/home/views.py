from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

def home(request):
    peoples=[
        {'name':'lalit kishor','age':26},
        {'name':'misaka kurosaki','age':41},
        {'name':'orihime kurosaki','age':19},
        {'name':'ichigo kurokaki','age':19},
        {'name':'gojo sotaru','age':26},
    ]
    return render(request, "index.html",context={'peoples':peoples})


def static_page(request):
    return HttpResponse("hey You ")
