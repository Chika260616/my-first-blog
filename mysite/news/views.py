from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import ArticleForm

# Create your views here.

def news_home(request):
    news = Article.objects.all()
    return render (request, 'news/news_home.html', {'news':news})

class NewsDetailView(DetailView):
    model = Article
    template_name= 'news/news_detail.html'
    context_object_name = 'article'

class NewsUpdateView (UpdateView):
    model = Article
    template_name= 'news/create.html'

    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name= 'news/news_delete.html'


class NewsUpdateView (UpdateView):
    model = Article
    template_name= 'news/create.html'

    form_class = ArticleForm


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticleForm()

    dato = {
        'form': form,
        'error': error,
    }
    return render (request, 'news/create.html', dato)