from qa.views import test, main_page, question, popular
from django.urls import path, re_path


urlpatterns = [
    # re_path(r'^$', test, name='root'),
    path('', main_page, name='main_page'),
    path('login/', test, name='login'),
    path('signup/', test, name='signup'),
    path('question/<int:question_id>/', question, name='question'),
    path('ask/', test, name='ask'),
    path('popular/', popular, name='popular'),
    path('new/', test, name='new')]
