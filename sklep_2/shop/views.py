from django.shortcuts import render
from django.http import HttpResponse
from django.test import client
from django.urls import reverse

def main(request):
    return render(request, 'base.html', {'main_bar': True})
