import requests
from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    '''Function to style up and support all functions from Home page'''
    my_projects =  Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':my_projects})

def internal_page(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'blog.html', {'project': project})


def all_news(request):
    base_url = 'https://newsapi.org/v2/everything'
    api_key = 'c664c9d23ee840dda61498959d1f4bc8'

    params = {
        'q':'tesla',
        'sortBy': 'published',
        # 'from': '2024-10-02',
        'apiKey': api_key
    }

    if 'number_news' in request.POST:
        number = request.POST['number_news']
        print("Got the Number of Articles from the page: ", number)
        response = requests.get(base_url, params=params, timeout=300)
        all_news = response.json()
        # print(all_news)
        articles = []
        print("Status code from the run: ", all_news['status'])
        if all_news['status'] == 'ok':
            print("Number of articles: ", len(all_news['articles']))
            print("First 2 FULL articles: ")
            # for a in all_news['articles']:
            #     print(a['title'])
            for i in all_news['articles']:
                articles.append(i['title'])
            print("First 10 articles: ",articles[:10])
            return render(request, 'portfolio/newspage.html', {"message": "Dispalying some news: ",
                                                            "news":articles[:int(number)]})
        else:
            print("Failed API call. See error bellow: \n", all_news['message'])
            return render(request, 'portfolio/newspage.html', {"message":"Could not get News via API."})
    else:
        return render(request, 'portfolio/newspage.html', {"message":"Please enter Number of News to return."})    


