from django import forms
from qa.models import Question, Answer


class AskForm (forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question_id = forms.IntegerField(widget=forms.HiddenInput())

    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a
