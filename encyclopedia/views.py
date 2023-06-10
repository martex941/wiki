from django.shortcuts import render, redirect
from django.contrib import messages
import re
import markdown2

from . import util


def index(request):

    entries = util.list_entries()

    if request.method == "POST":
        query = request.POST.get("q")
        if query in entries:
            return redirect("entry", entry_name=query)
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
        return redirect("no_entry")

    return render(request, "encyclopedia/entry.html", {
        "current_entry": current_entry
    })

def new_page(request):
    if request.method == "POST":
        entries = util.list_entries()
        entry_title = request.POST.get("entry-title")
        entry_contents = request.POST.get("entry-contents")
        
        if entry_title in entries:
            messages.error(request, "ERROR: The entry title already exists in the database.")
        else:
            util.save_entry(entry_title, entry_contents)
            return redirect("entry", entry_name=entry_title)
        
    return render(request, "encyclopedia/new_page.html")
    
def edit_page(request):

    return render(request, "encyclopedia/edit_entry.html")