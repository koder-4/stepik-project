from django import forms
from qa.models import Question, Answer, User
from django.shortcuts import get_object_or_404


class AskForm (forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question(**self.cleaned_data, author=self._user)
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    # def clean_question(self):
    #     return get_object_or_404(Question, self.cleaned_data['question'])

    def save(self):
        q = get_object_or_404(Question, pk=self.cleaned_data['question'])
        a = Answer(question=q, text=self.cleaned_data['text'], author=self._user)
        a.save()
        return a


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        u = User.objects.create_user(**self.cleaned_data)
        return u
