from django.shortcuts import render
from .models import Topic, Tag, Question, VarList, Relative, RelInitial, Comment
from .forms import QuestionForm, QuImageFormSet, CommentFormSet, CoImageFormSet, CoFileFormSet
from .forms import VarFormSet, LetterFormSet
from .scripts import quicksave
from django.core.paginator import Paginator

import git
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo('/home/newbioquest/bioquest')
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

def index(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def add(request):

    if request.method == 'POST':

        addform = QuestionForm(request.POST)

        question = quicksave(addform)

        if question:
            quimages = QuImageFormSet(request.POST, request.FILES, instance=question)
            addform.save()
            for im in quimages:
                quicksave(im)


            commentform = CommentFormSet(request.POST, request.FILES, instance=question)
            comment = quicksave(commentform)

            if comment:
                for el in comment:

                    coimages = CoImageFormSet(request.POST, request.FILES, instance=el)
                    for im in coimages:
                        quicksave(im)

                    cofiles = CoFileFormSet(request.POST, request.FILES, instance=el)
                    for f in cofiles:
                        quicksave(f)

                commentform.save()

            varform = VarFormSet(request.POST, instance = question)
            quicksave(varform)

            letterform = VarFormSet(request.POST, instance = question)
            letter = quicksave(letterform)

        if question and quimages:
            return redirect('problems')

    addform = QuestionForm()
    quimage = QuImageFormSet()
    comment = CommentFormSet()
    coimage = CoImageFormSet()
    cofile = CoFileFormSet()

    var = VarFormSet()
    letter = LetterFormSet()

    context = {'addform': addform,
    'quimage': quimage,
    'comment': comment,
    'coimage': coimage,
    'cofile': cofile,
    'var': var,
    'letter': letter}

    return render(request, 'add.html', context)

def instructions(request):
    return render(request, 'instructions.html')

def personal(request):
    return render(request, 'personal.html')

def problems(request):

    search = request.GET.get('search', '')
    questions = Question.objects.order_by('-id')
    tags = Tag.objects.all()
    topic = request.GET.get('topic', '')

    paginator = Paginator(questions, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    context = {
        'title': 'Вопросы',
        'questions': page, 'tags': tags,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'search': search,
        'topic': topic
        }

    return render(request, 'problems.html', context = context)
