from django.shortcuts import render
from django.views import View

# Create your views here.

class HelloView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'hello.html', {})


hello = HelloView.as_view() # shows templates/hello.html
