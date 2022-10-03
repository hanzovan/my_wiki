from django.shortcuts import render
from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_name):

    entry = util.get_entry(entry_name)
    
    if not entry:
        return render(request, "encyclopedia/error.html", {
            "message": "None"
        })

    else:

        content = markdown(entry)

        return render(request, "encyclopedia/entry.html", {
            "entry": entry_name,
            "content": content
        })