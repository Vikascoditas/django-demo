from django.http import HttpResponse


HTML_STRING="""
<h1> Hello Vikas it is main page </h1>
"""

HTML_STRING_FOR_ABC="""
<p> Hello Vikas it is main page abc </p>
"""
def home_view(request):
    return HttpResponse(HTML_STRING)

def home_abc(request):
    return HttpResponse(HTML_STRING_FOR_ABC)



