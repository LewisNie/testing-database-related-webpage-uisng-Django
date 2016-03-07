from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

# view used by the catalog app
from .models import Publisher, Title
from .forms import PublisherForm, TitleForm, PublisherSearchForm, TitleSearchForm

def index(request):
    ''' Index page to provide links to the different options
    '''
    return render(request, 'index.html')

# Sloppy versions of the views -- a lot of duplicate code :(
def add_publisher(request):
    ''' View to add a publisher
    '''
    # edited from code on https://docs.djangoproject.com/en/1.8/topics/forms/
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PublisherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            form.save()
            return HttpResponseRedirect('/catalog/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PublisherForm()

    return render(request, 'add_publisher.html', {'form': form})

def add_title(request):
    ''' View to add a title -- needs publisher to have already been added
    '''
    # edited from code on https://docs.djangoproject.com/en/1.8/topics/forms/
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TitleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            form.save()
            return HttpResponseRedirect('/catalog/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TitleForm()

    return render(request, 'add_title.html', {'form': form})

def get_titles_by_publisher(request):
    ''' View to find titles of a specific publisher
    '''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PublisherSearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            target_publisher = form.cleaned_data['publisher']
            try:
                publisher = Publisher.objects.get(pub_name=target_publisher)
                title_list = Title.objects.filter(pub_id=publisher.pub_id)
            except Publisher.DoesNotExist:
                publisher = None
            return render(request, 'get_titles_by_publisher.html', {'result':True, 'publisher': publisher, 'title_list': title_list})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PublisherSearchForm()

    return render(request, 'get_titles_by_publisher.html', {'form': form})

def get_publisher_of_title(request):
    ''' View to find publisher of a specific title
    '''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TitleSearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            target_title = form.cleaned_data['title']
            try:
                publisher = Title.objects.get(title=target_title)
            except Title.DoesNotExist:
                publisher = None
            return render(request, 'get_publisher_of_title.html', {'result':True, 'publisher': publisher})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TitleSearchForm()

    return render(request, 'get_publisher_of_title.html', {'form': form})
