from django.shortcuts import render
import random
from . import util
from markdown2 import Markdown

markdowner = Markdown()


def index(request):
    print(util.list_entries())
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    page = util.get_entry(title)
    if page:
        return render(request, 'encyclopedia/details.html', {
            'page': markdowner.convert(page),
            'title': title,
        })
    else:
        return render(request, 'encyclopedia/errors.html', {'message': 'Page not found'})


def search(request):
    print(request.GET['q'], '🌹🌹🌹')
    title = request.GET['q']
    page = util.get_entry(title)
    if page:
        return render(request, 'encyclopedia/details.html', {
            'page':  markdowner.convert(page),
            'title': title,
        })
    else:
        return render(request, 'encyclopedia/errors.html', {'message': 'Page not found'})


def create(request):
    if request.method == "GET":
        print(request.GET)
        return render(request, 'encyclopedia/create.html')
    else:
        # print('🌹🌹🌹')
        # print(request.POST['title'])
        # print(request.POST['content'])
        title = request.POST['title']
        if util.get_entry(title):
            return render(request, 'encyclopedia/errors.html', {'message': 'Page alerady exists'})
        content = request.POST['content']
        util.save_entry(title, content)
        page = util.get_entry(title)
    return render(request, 'encyclopedia/details.html', {
        'page':  markdowner.convert(page),
        'title': title,
    })


def edit(request, title):
    page = util.get_entry(title)
    if request.method == 'GET':
        return render(request, 'encyclopedia/edit-page.html', {
            'page':  markdowner.convert(page),
            'title': title,
        })
    else:
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        page = util.get_entry(title)
    return render(request, 'encyclopedia/details.html', {
        'page':  markdowner.convert(page),
        'title': title,
    })


def random_page(request):
    n = random.randint(0, len(util.list_entries())-1)
    title = util.list_entries()[n]
    page = util.get_entry(title)
    return render(request, 'encyclopedia/details.html', {
        'page':  markdowner.convert(page),
        'title': title,
    })
