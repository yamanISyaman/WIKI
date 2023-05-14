import markdown2
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from . import util


class EntryTextForm(forms.Form):
    title = forms.CharField(label="Title")


def index(request):
    q = request.GET.get("q")
    if q:
        entries = util.list_entries()
        results = []

        for entry in entries:
            if q == entry:
                return HttpResponseRedirect(f"/{q}")
            elif q in entry:
                results.append(entry)

        if results:
            return render(request, "encyclopedia/index.html", {
                "entries": results,
                "heading": "Search Results",
            })
        else:
            return HttpResponse("NO RESULTS")

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
        return render(request, "encyclopedia/404.html", {"pagename": pagename})


def add_entry(request):
    if request.method == "POST":
        title = request.POST.get("title")
        entry = request.POST.get("entry")
        util.save_entry(title, entry)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "encyclopedia/entrypage.html", {
        "title": "Add Entry",
        "form": EntryTextForm(),
        "button": "Add"
    })
