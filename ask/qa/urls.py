from qa.views import test
from django.urls import path, re_path


urlpatterns = [
    re_path(r'^$', test, name='root'),
    path('login/', test, name='login'),
    path('signup/', test, name='signup'),
    path('question/<dec>/', test, name='question'),
    path('ask/', test, name='ask'),
    path('popular/', test, name='new'),
    path('new/', test, name='new')]
