from django import forms
from django.shortcuts import render
from django.shortcuts import render
from django.template import RequestContext
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required



class IndexView(View):
    def get(self, request):
        # theme = request.theme
        template = f"themes/work/index.html"
        return render(request, template, {})