from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm


def test(request):
    return HttpResponse('OK')


def main_page(request):
    questions = Question.objects.new()
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/main_page.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })


def question(request, question_id):
    qq = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            a = form.save()
            url = '/question/%d/' % a.question.id
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'qa/question.html', {'q': qq, 'form': form})


def popular(request):
    questions = Question.objects.popular()
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/popular.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            url = '/question/%d/' % q.id
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html',
                  {'form': form})
