import markdown2
from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def getpage(request, pagename):
    html = markdown2.markdown(util.get_entry(pagename))
    if html:
        return render(request, html)
    else:
        return render(request, "encyclopedia/404.html", {
"pagename": pagename
    })

