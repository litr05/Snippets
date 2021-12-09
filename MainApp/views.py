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


def snippet_delete(request, id):
    p = Snippet.objects.get(id=id)
    p.delete()
    return redirect('snippets-list')


def single_snippet_page(request, id):
    try:
        snippets = Snippet.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    context = {'pagename': 'Страница сниппета',
               'snippet': snippets,
               "type": "view",
               }
    return render(request, 'pages/snippet_page.html', context)


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


def snippet_edit(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    if request.method == "GET":
        context = {
            'pagename': 'Редактировать сниппет',
            "snippet": snippet,
            "type": 'edit'
        }
        return render(request, 'pages/snippet_page.html', context)

    if request.method == "POST":
        form_data = request.POST
        snippet.name = form_data["name"]
        snippet.creation_date = form_data["creation_date"]
        snippet.code = form_data["code"]
        snippet.save()
        snippets = Snippet.objects.all()
        context = {'pagename': 'Просмотр сниппетов',
                   'snippets': snippets,
                   }
        return render(request, 'pages/view_snippets.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass

    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')