from django.shortcuts import render
from django.http import HttpResponseRedirect
import re
import markdown2

from . import util


def index(request):

    entries = util.list_entries()

    if request.method == "POST":
        query = request.POST.get("q")
        if query in entries:
            return HttpResponseRedirect(query)
        else:
            pattern = rf'.*{query}.*'
            matched_entries = [item for item in entries if re.match(pattern, item, re.IGNORECASE)]
            return render(request, "encyclopedia/search_results.html", {"matched_entries":matched_entries, "query": query})
        
    return render(request, "encyclopedia/index.html", {
        "entries": entries
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


    
