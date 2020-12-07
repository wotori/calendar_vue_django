from django.shortcuts import render


def index(request):
    context = {'calendar_data': 'appears_here'}
    return render(request, 'calendar_api/index.html', context)
