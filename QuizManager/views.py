from django.shortcuts import redirect, render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages

from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import logout as auth_logout

from .models import Choice, Question, Quiz

from .forms import QuizModelForm, UserLoginForm, QuestionChoiceFormset, QuestionModelForm

def index(request):
    if not request.user.is_authenticated:
        return redirect('QuizManager:login')
    quizzes = Quiz.objects.all()
    context = {
        'quizzes' : quizzes
    }
    return render(request, 'QuizManager/index.html', context)

def edit_question(request, id):
    question = get_object_or_404(Question, pk=id)
    form = QuestionModelForm(request.POST or None,instance=question)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('QuizManager:view_question', id=id)
    context = {
        'form' : form,
        'question' : question,
        'id' : id
    }
    return render(request, 'QuizManager/edit_question.html', context)

def view_question(request, id):
    question = get_object_or_404(Question, pk=id)
    context = {
        'question' : question
    }
    return render(request, 'QuizManager/view_question.html', context)

def edit_choices(request, id):
    question = Question.objects.get(id=id)
    formset = QuestionChoiceFormset(instance=question)
    if request.method == 'POST':
        formset = QuestionChoiceFormset(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            return redirect('QuizManager:view_question', id=id)
    context = {
        'question' : question,
        'formset' : formset,
        'id' : id
    }
    return render(request, 'QuizManager/edit_choices.html', context)

def add_question(request):
    if request.method == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('QuizManager:view_question', id=question.id)
    else:
        form = QuestionModelForm()
    context = {
        'form' : form
    }
    return render(request, 'QuizManager/add_question.html', context)

def add_quiz(request):
    if request.method == 'POST':
        form = QuizModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('QuizManager:index')
    else:
        form = QuizModelForm
    context = {
        'form' : form
    }
    return render(request, 'QuizManager/add_quiz.html', context)

def view_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    questions = quiz.questions.all()
    context = {
        'questions' : questions
    }
    return render(request, 'QuizManager/view_quiz.html', context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth_authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('QuizManager:index')
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = UserLoginForm()
    context ={
        'form' : form
    }
    return render(request,"QuizManager/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect('QuizManager:login')