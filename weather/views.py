from django.shortcuts import render
from .data import weather_search
from .models import weather_data
from .form import search_bar
from django.core.paginator import Paginator

def WeatherView(request):
    c_data = '0'
    f_data = '0'
    output = ''
    location = ""
    form = search_bar(request.POST or None)
    if form.is_valid():
        location = form.cleaned_data['location']
        form = search_bar()
        if '°' not in weather_search(location):
            output = "No Data Found"
        else:
            output = weather_search(location)
            info = weather_data(location=location)
            c_data = output
            eq = c_data.replace('°', '')
            e = eq.replace('C', '')
            f_data = f'{(int(e) *  9/5) + 32} °F'
            info.save()

    context = {
        'c_data':c_data,
        'f_data': f_data,
        'output':output,
        'form': form,
        'location':(location.capitalize)
        }
    return render(request, 'weather.html', context)

def around_world(request):
    place_list = ['London', 'New York City', 'Paris', 'Moscow', 'Tokyo', 'Dubai', 'Singapore',
    'Barcelona', 'Los Angeles', 'Madrid', 'Rome', 'Chicago', ' Toronto', 'San Francisco',
    'Abu Dhabi', 'Kolkata', ' St. Petersburg', 'Amsterdam', 'Berlin','Istanbul', 'New Delhi', 'Las Vegas',
    'Mumbai']
    c_data = []
    for x in place_list:
        data = weather_search(x)
        eq = data.replace('°', '')
        e = eq.replace('C', '')
        f_data = f'{(int(e) *  9/5) + 32} °F'
        c_data.append([x, data, f_data])

    paginator = Paginator(c_data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj
    }
    return render(request, 'weather_world.html', context)