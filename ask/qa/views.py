from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from qa.models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main_page(request, *args, **kwargs):
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
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/question.html', {question: q})



def popular(request, *args, **kwargs):
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
