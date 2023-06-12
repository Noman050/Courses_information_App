import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.urls import reverse



def list_topics():
    _, filenames = default_storage.listdir("topics")
    return list(sorted(re.sub(r"\.txt$", "", filename)
                for filename in filenames if filename.endswith(".txt")))


def save_topic(title, content):
    filename = f"topics/{title}.txt"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
    return redirect('outline/index.html')


def get_topic(title):
    try:
        f = default_storage.open(f"topics/{title}.txt")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
