import markdown2
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from . import util


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
            "html": markdown2.markdown(html)
})
    else:
        return render(request, "encyclopedia/404.html", {"pagename": pagename})
