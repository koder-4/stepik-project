from django.http import HttpResponse


def test (request, *args, **kwargs):
    return HttpResponse('OK')

def main_page(request, *args, **kwargs):
    return HttpResponse('OK')
	
def question(request, *args, **kwargs):
    return HttpResponse('OK')

def popular(request, *args, **kwargs):
    return HttpResponse('OK')