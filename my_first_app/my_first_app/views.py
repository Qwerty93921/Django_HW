from django.shortcuts import render


def index(request):
    return render(request, 'file_from_temlates.html', context={})