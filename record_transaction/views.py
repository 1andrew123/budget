from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Hello, world. You're at the record_transaction index.</h2>")

