from django.shortcuts import render
from bachelor_projects.models import Article

def index(request):
    articles = Article.objects.all()
    for article in articles:
        print(article.title)


    return render(request, 'index.html', {'articles' : articles})

def about(request):
    return render(request, 'about.html')

def post(request):
    return render(request, 'post.html')

def post(request, id_post):
    article = Article.objects.get(pk=id_post)
    return render(request, 'post.html', {'article' : article})

def contact(request):
    return render(request, 'contact.html')
    