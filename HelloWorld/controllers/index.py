# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    view_data = {}
    view_data['hello'] = 'Hello World!'
    return render(request, 'index.html', view_data)
