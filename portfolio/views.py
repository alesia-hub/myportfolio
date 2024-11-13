import requests
from django.shortcuts import render
from .models import Project

def home(request):
    '''Function to style up and support all functions from Home page'''
    my_projects =  Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':my_projects})

def all_news(request):
    base_url = 'https://newsapi.org/v2/everything'
    api_key = 'c664c9d23ee840dda61498959d1f4bc8'

    params = {
        'q':'tesla',
        'sortBy': 'published',
        'from': '2024-10-02',
        'apiKey': api_key
    }

    response = requests.get(base_url, params=params, timeout=300)
    all_news = response.json()
    # print(all_news)
    articles = []
    print("Status code from the run: ", all_news['status'])
    if all_news['status'] == 'ok':
        print("Number of articles: ", len(all_news['articles']))
        for i in all_news['articles']:
            articles.append(i['title'])
            #print(all_news['articles'][0]['description'])
    else:
        print("Failed API call. See error bellow: \n", all_news['message'])
    return render(request, 'portfolio/newspage.html', {"news":articles[1:6]})
