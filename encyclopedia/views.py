import markdown2
from django.http import HttpResponse
from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def getpage(request, pagename):
    html = util.get_entry(pagename)
    if html:
        return HttpResponse(markdown2.markdown(html))
    else:
        #return HttpResponse("error 404")
        return render(request, "encyclopedia/404.html", {
"pagename": pagename
    })

