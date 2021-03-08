from django.shortcuts import render
from .models import country_data
from .data import country_info
from .form import search_bar

def InfoView(request):
    data = ''
    country = ''
    form = search_bar(request.POST or None)
    if form.is_valid():
        country = form.cleaned_data['country']
        form = search_bar()
        data = country_info(country)
        if data[0] != 'No Data Found':
            info = country_data(country=country)
            info.save()
    context = {
        'data':data, 
        'form':form,
        'country': country
    }
    return render(request, 'info.html', context)
        