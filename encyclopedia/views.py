import markdown2
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from random import choice
from . import util


class EntryTextForm(forms.Form):
    title = forms.CharField(label="Title")


def index(request):
    q = request.GET.get("q")
    if q:
        q = q.upper()
        entries = util.list_entries()
        results = []

        for entry in entries:
            if q == entry.upper():
                return HttpResponseRedirect(f"/{entry}")
            elif q in entry.upper():
                results.append(entry)

        if results:
            return render(request, "encyclopedia/index.html", {
                "entries": results,
                "heading": "Search Results",
            })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": results,
                "heading": "No Results",
            })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "heading": "All Pages",
    })


def getpage(request, pagename):
    
    html = util.get_entry(pagename)
    if html:
        return render(request, "encyclopedia/entries.html", {
            "pagename": pagename,
            "html": markdown2.markdown(html),
            "data": ""
        })
    else:
        return render(request, "encyclopedia/404.html", {"error": f'''the page \"{pagename}\" was not found'''})


def add_entry(request):
    if request.method == "POST":
        title = request.POST.get("title")
        entry = request.POST.get("entry")
        ls = [i.upper() for i in util.list_entries()]
        if title.upper() in ls:
            return render(request, "encyclopedia/404.html", {"error": f'''An entry with the title \"{title}\" already exists'''})
        util.save_entry(title, entry)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "encyclopedia/entrypage.html", {
        "title": "Add Entry",
        "form": EntryTextForm(),
        "button": "Add",
        "url": "addentry",
    })


def edit_entry(request, name):
    if request.method == "POST":
        title = name
        entry = request.POST.get("entry")        
        util.save_entry(title, entry)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "encyclopedia/entrypage.html", {
        "title": "Edit Entry",
        "button": "Edit",
        "url": "edit",
        "data": util.get_entry(name),
        "name": name
    })


def rand_page(request):
    return getpage(request, choice(util.list_entries()))