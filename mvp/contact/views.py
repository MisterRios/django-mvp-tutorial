from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import ContactView
from django.contrib import messages

def contact(request):
	form = ContactView(request.POST or None) 
	#what you get from the form via POST
	if form.is_valid():
		our_form = form.save(commit=False)
		our_form.save() #new version of form if valid
		messages.add_message(request, messages.INFO, 'Your message has been sent. Thank you.')
		return HttpResponseRedirect('/')
	t = loader.get_template('contact.html')
	c = RequestContext(request, { 'form' : form ,})
	return HttpResponse(t.render(c))
	#syntax is essentially HttpResponse(loader.get_template('contact.html').render(RequestContext(request, {'form' = form , })))
