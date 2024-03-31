from django.views.generic import TemplateView
from django.shortcuts import render

class page(TemplateView):
    template_name = 'personschedule.html'
    def post(self, request):
        
        return render(request, self.template_name, {})