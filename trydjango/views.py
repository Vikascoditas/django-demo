from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string,get_template
import random




def home_view(request,*args,**kwargs):
    print(*args,*kwargs )
    article_obj_queryset = Article.objects.all()
    random_id=random.randint(1,4)
    article_obj=Article.objects.get(id=random_id)
    context={
        "object_list":article_obj_queryset,
        "title":article_obj.title,
        "id":article_obj.id,
        "content":article_obj.content
    }
    tmpl=get_template("home-view.html")
    HTML_STRING=render_to_string("home-view.html",context=context)

    return HttpResponse(HTML_STRING)


