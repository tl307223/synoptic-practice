from django.shortcuts import redirect, render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages

from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import logout as auth_logout

from .models import Choice, Question, Quiz, Result

from .forms import QuizModelForm, UserLoginForm, QuestionChoiceFormset, QuestionModelForm, AnswerQuestionForm


def index(request):
    if not request.user.is_authenticated:
        return redirect('QuizManager:login')
    quizzes = Quiz.objects.all()
    context = {
        'quizzes' : quizzes
    }
    return render(request, 'QuizManager/index.html', context)

def view_quizzes(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes' : quizzes
    }
    return render(request, 'QuizManager/view_quizzes.html', context)


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
    quiz_id = question.quiz.id
    context = {
        'question' : question,
        'quiz_id' : quiz_id
    }
    return render(request, 'QuizManager/view_question.html', context)

def edit_choices(request, id):
    question = get_object_or_404(Question, pk=id)
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

def add_question(request, quiz=None):
    if request.method == 'POST':
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('QuizManager:view_question', id=question.id)
    elif quiz:
        initial_quiz = get_object_or_404(Quiz, pk=quiz)
        form = QuestionModelForm(initial={'quiz' : quiz })
    else:
        form = QuestionModelForm()
    context = {
        'form' : form
    }
    return render(request, 'QuizManager/add_question.html', context)

def delete_question(request, id):
    question = get_object_or_404(Question, pk=id)
    quiz = question.quiz.id
    question.delete()
    return redirect('QuizManager:view_quiz', id=quiz)

def add_quiz(request):
    if request.method == 'POST':
        form = QuizModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('QuizManager:view_quizzes')
    else:
        form = QuizModelForm
    context = {
        'form' : form
    }
    return render(request, 'QuizManager/add_quiz.html', context)

def view_quiz(request, id):
    quiz = get_object_or_404(Quiz, pk=id)
    questions = quiz.questions.all()
    context = {
        'quiz' : quiz,
        'questions' : questions
    }
    return render(request, 'QuizManager/view_quiz.html', context)

def edit_quiz(request, id):
    quiz = get_object_or_404(Quiz, pk=id)
    form = QuizModelForm(request.POST or None,instance=quiz)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('QuizManager:view_quiz', id=quiz.id)
    context = {
        'quiz' : quiz,
        'form' : form,
    }
    return render(request, 'QuizManager/edit_quiz.html', context)

def delete_quiz(request, id):
    quiz = get_object_or_404(Quiz, pk=id)
    quiz.delete()
    return redirect('QuizManager:view_quizzes')

def take_quiz(request, id):
    quiz = get_object_or_404(Quiz, pk=id)
    if request.method == 'POST':
        choices = request.POST.getlist('choices')
        score = 0
        for choice in choices:
            choice_object = Choice.objects.get(pk=int(choice))
            if choice_object.correct:
                score += 1
        result_obj = Result(quiz=quiz, user=request.user, score=score)
        result_obj.save()
        request.user.assigned_quizzes.remove(quiz)
        return redirect('QuizManager:quiz_results', id=result_obj.pk)
    questions = quiz.questions.all()
    forms = [AnswerQuestionForm(question) for question in questions]
    context = {
        'quiz' : quiz,
        'questions' : questions,
        'forms' : forms
    }
    return render(request, 'QuizManager/take_quiz.html', context)

def quiz_results(request, id):
    result = get_object_or_404(Result, pk=id)
    max_score = result.quiz.questions.count()
    context = {
        'max_score' : max_score,
        'result' : result
    }
    return render(request, 'QuizManager/quiz_results.html', context)


def view_assigned_quizzes(request):
    assigned_quizzes = request.user.assigned_quizzes.all()
    context = {
        'assigned_quizzes' : assigned_quizzes
    }
    return render(request, 'QuizManager/view_assigned_quizzes.html', context)

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