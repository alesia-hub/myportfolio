import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from utils.DBConnect import MongoConnect
from .models import Project, Blog

dbClient = MongoConnect("mongodbVSCodePlaygroundDB")
CollectionGame = "GameData"

def home(request):
    '''Function to style up and support all functions from Home page'''
    my_projects =  Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':my_projects})

def internal_page(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'blog.html', {'project': project})


def about_projects(request):
    all_projects = Blog.objects.all()  # will show All ogbejct from DB
    # If you want to show only first 5 items from DB on the page use this:
    # all_projects = Blog.objects.order_by('-date')[:5]
    print(all_projects)
    return render(request, 'portfolio/aboutprojects.html',
                  {'message': "List of all implemented projects",
                   'all_projects': all_projects})


def all_news(request):
    base_url = 'https://newsapi.org/v2/everything'
    api_key = 'c664c9d23ee840dda61498959d1f4bc8'

    params = {
        'q':'Africa',
        'sortBy': 'published',
        # 'from': '2024-10-02',
        'apiKey': api_key
    }

    if 'number_news' in request.POST:
        number = request.POST['number_news']
        topic = request.POST['topic']
        params = {
            'q':str(topic),
            'sortBy': 'published',
            # 'from': '2024-10-02',
            'apiKey': api_key
        }
        
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
            return render(request, 'portfolio/newspage.html', {"message": "Dispalying news headlines: ",
                                                            "news":articles[:int(number)]})
        else:
            print("Failed API call. See error bellow: \n", all_news['message'])
            return render(request, 'portfolio/newspage.html', {"message":"Could not get News via API."})
    else:
        return render(request, 'portfolio/newspage.html', \
                      {"message":"Please enter Number of News to return."})

def game_questions(request):
    # dbClient = MongoConnect("mongodbVSCodePlaygroundDB")
    # CollectionGame = "GameData"

    if 'Question' in request.POST:
        question = request.POST['Question']
        print("*** Got the Number of Articles from the page: ", question)
        level = request.POST['level']
        ans1 = request.POST['option1']
        ans2 = request.POST['option2']
        ans3 = request.POST['option3']
        ans4 = request.POST['option4']
        answer = request.POST['answer']
        _record = {
            'question': question,
            'options': [ans1, ans2, ans3, ans4],
            'answer': answer,
            'level': level
        }
        
        print("*** Got All Details:", _record)

        dbClient.insert_into_collection(CollectionGame, _record)

        return render(request, 'portfolio/questions.html', \
                      {"message":"Question was received successfully."})
    else:
        return render(request, 'portfolio/questions.html', \
                      {"message":"Please enter valid question details"})


def play_game(request):
    # filters = {"level": "90%"}
    # _question = dbClient.read_doc_from_collection(CollectionGame, filters)
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == "level_form":
            level = request.POST['questionLevel']
            print("*** Got Level: ", level)
            filters = ({"level": level})
            _question = dbClient.read_doc_from_collection(CollectionGame, filters)
            request.session['question'] = _question['question']
            request.session['answer'] = _question['answer']

            print("*** got DB response: ", _question)
            return render(request, 'portfolio/gameplay.html', \
                {"message":"Here is your question: ",
                "question": _question["question"]})

        elif form_type == "answer_form":
            my_question = request.session.get('question')
            my_answer = request.session.get('answer')
            if not my_question:
                return HttpResponse("Session expired or question not available.")
            
            answer = request.POST.get('answer')
            is_correct = False
            if answer == my_answer:
                is_correct = True
                
            return render(request, 'portfolio/gameplay.html', \
                        {"message":"Here is your question: ",
                        "question": my_question,
                        "your_answer": f"Your answer: {answer}",
                        "is_correct": is_correct,
                        "answers": f"Actual answer is: {my_answer}",})
        else:
            return render(request, 'portfolio/gameplay.html', \
                      {"message":"Here is your question: ",
                       "question": _question["question"]})

    else:
        return render(request, 'portfolio/gameplay.html', \
                      {"message":"Select question level: "})
