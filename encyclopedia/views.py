from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2

from . import util


def index(request):

    if request.method == "POST":
        query = request.POST.get("q")
        return HttpResponseRedirect(query)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def no_entry(request):
    return render(request, "encyclopedia/no_entry.html")

def entry(request, entry_name):

    try:
        current_entry = util.get_entry(entry_name)
        current_entry = markdown2.markdown(current_entry)
    except TypeError:
        return HttpResponseRedirect("no_entry")

    return render(request, "encyclopedia/entry.html", {
        "current_entry": current_entry
    })

