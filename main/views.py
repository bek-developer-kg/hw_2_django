from django.shortcuts import render

# Create your views here.
def main(request):
    context = {
        "title": "Backend",
        "name": "Бекзат Касымов",
        "info": "4 месяц бэкенд",
        "bio": "биография"

    }
    return render(request, 'index.html', context=context)
def mix(request):
    context = {
        "title": "Designer",
        "name": "Аман",
        "info": "my friend",
        "bio": "no infornation"
    }
    return render(request, 'homework.html', context=context)