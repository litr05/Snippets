from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов',
               'snippets': snippets,
               }
    return render(request, 'pages/view_snippets.html', context)


def single_snippet_page(request, id):
    try:

        snippets = Snippet.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    context = {'pagename': 'Страница сниппета',
               'snippet': snippets,
               }
    return render(request, 'pages/snippet_page.html', context)


def create_new_snippet(request):
    form_data = request.POST
    snippet = Snippet(name=form_data["name"], lang=form_data["lang"], code=form_data["code"])
    snippet.save()
    return redirect('snippets-list')


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request, 'add_snippet.html', {'form': form})
