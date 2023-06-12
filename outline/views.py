from django.shortcuts import render, redirect
from .util import get_topic, list_topics
import markdown2
import random
from .util import save_topic

# Topic Page
def topic_view(request, title):
    topic_content = get_topic(title)
    if topic_content is None:
        return render(request, 'outline/error_page.html', {
            'message': "Course Not Found Please Try A Different One"
        })
    
    html_content = markdown2.markdown(topic_content)
    context = {
        'title': f"Course Outline - {title}",
        'plain': f'{title}',
        'content': html_content
    }
    return render(request, 'outline/topic_page.html', context)


# Index Page
def index_view(request):
    topics = list_topics()
    context = {
        'topics': topics
    }
    return render(request, 'outline/index_page.html', context)

def search_view(request):
    if request.method == 'POST':
        query = request.POST['query']
        topic_content = get_topic(query)
        # if topic_content is not None:
        #     return redirect('topic_page', title=query)
        # else:
        topics = list_topics()
        filtered_topics = list(filter(lambda x: query in x, topics))
        context = {
            'query': query,
            'topics': filtered_topics
        }
        return render(request, 'outline/search_results.html', context)
    else:
        return redirect('outline/search_page.html')


# New Page
def new_page_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        
        if get_topic(title) is not None:
            return render(request, 'outline/error_page.html', {'message': 'Topic already exists.'})
        
        save_topic(title, content)
        return redirect('topic_page', title=title)
    else:
        return render(request, 'outline/new_page.html')


# Edit Page
def edit_page_view(request, title):
    topic_content = get_topic(title)
    if topic_content is None:
        return render(request, 'outline/error_page.html', {
            'message':"Error: Topic Content is none."
        })
    
    if request.method == 'POST':
        new_content = request.POST['content']
        save_topic(title, new_content)
        return redirect('topic_page', title=title)
    else:
        context = {
            'title': title,
            'content': topic_content
        }
        return render(request, 'outline/edit_page.html', context)


# Random Page
def random_page_view(request):
    topics = list_topics()
    random_topic = random.choice(topics)
    return redirect('topic_page', title=random_topic)
