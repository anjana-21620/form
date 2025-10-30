from django.shortcuts import render
from.models import*
from .forms import *

# Create your views here.
def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = ContactForm()  # clear form after saving
    return render(request, 'contact.html', {'form': form})


def contact_list(request):
    contacts = contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})