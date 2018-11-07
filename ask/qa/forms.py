from django import forms
from qa.models import Question, Answer
from django.shortcuts import get_object_or_404


class AskForm (forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    # def clean_question(self):
    #     return get_object_or_404(Question, self.cleaned_data['question'])

    def save(self):
        q = get_object_or_404(Question, pk=self.cleaned_data['question'])
        a = Answer(question=q, text=self.cleaned_data['text'], author=None)
        a.save()
        return a
