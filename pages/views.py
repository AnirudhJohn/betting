from re import template
from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class StagingAreaView(TemplateView):
    template_name = 'stage.html'
class NewHome(TemplateView):
    template_name = 'betting.html'
