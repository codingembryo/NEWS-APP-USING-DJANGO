from django.shortcuts import render
import requests
API_KEY = 'ac703666d57a49e784c0293bf0dac515'


def home(request):
    country = request.GET.get('country')

    category = request.GET.get('category')

    if country:

        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

        articles = data['articles']

    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()

        articles = data['articles']


    context = {
        'articles': articles
    }
    
    return render(request, 'newsappi/home.html', context)




