from qa.views import test, main_page, question, popular, ask, login, signup
from django.urls import path, re_path


urlpatterns = [
    # re_path(r'^$', test, name='root'),
    path('', main_page, name='main_page'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('login', login, name='lg'),
    path('signup', signup, name='su'),
    path('question/<int:question_id>/', question, name='question'),
    path('question/<int:question_id>', question, name='qs'),
    path('ask/', ask, name='ask'),
    path('popular/', popular, name='popular'),
    path('new/', test, name='new')]
