from email.headerregistry import ContentTypeHeader
from django.shortcuts import render
from markdown2 import markdown
from django.http import HttpResponseRedirect
from django.urls import reverse
import os
from random import choice

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
            "title": entry_name,
            "content": content
        })

def search(request):

    query = request.POST["q"]

    result = util.get_entry(query)

    if not result:

        entries = util.list_entries()
        match = []

        for entry in entries:
            if query.lower() in entry.lower():
                match.append(entry)

        return render(request, "encyclopedia/search.html", {
            "query": query,
            "matchs": match
        })

    else:
        return render(request, "encyclopedia/entry.html", {
            "title": query,
            "content": markdown(result)
        })


def new(request):

    # if user reached route by submiting form
    if request.method == "POST":
        title = request.POST["title"]

        # if title already existed, show error message
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "This title is already existed!!!"
            })
        
        # if title doesn't exist, save new file
        else:


            content = request.POST["content"]
            file = open(f"entries/{title}.md", "w")
            file.write(content)
            file.close()

            # Get entry from storage

            new_content = util.get_entry(title)      
        
            # Redirect user to the new entry
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": markdown(new_content)
            })

    # if user reached route via clicking link, show the form
    else:
        return render(request, "encyclopedia/new.html")


def edit(request, name):

    # if user reached route by submiting form:
    if request.method == "POST":

        # remove the old file
        os.remove(f"entries/{name}.md")

        content = request.POST["detail"]
        title = request.POST["title"]
        file = open(f"entries/{title}.md", "w")
        file.write(content)
        file.close()        

        # redirect user to the entry
        new_content = util.get_entry(title)

        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdown(new_content)
        })

    # if user reached route by clicking link:
    else:

        # Get the content from name
        content = util.get_entry(name)

        return render(request, "encyclopedia/edit.html", {
            "title": name,
            "content": content
        })

def remove(request):
    if request.method == "POST":
        title = request.POST["re"]
        
        # remove the file from storage
        os.remove(f"entries/{title}.md")

        return HttpResponseRedirect(reverse("encyclopedia:index"))

def rando(request):
    choices = util.list_entries()
    chosen = choice(choices)

    content = util.get_entry(chosen)

    # render the entry
    return render(request, "encyclopedia/entry.html", {
        "title": chosen,
        "content": markdown(content)
    })