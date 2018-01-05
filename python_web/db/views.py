# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# 跳转至页面
from django.utils.translation import ugettext_lazy as _
def skip(request):
    return render(request, "test.html")