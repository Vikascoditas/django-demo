from django.shortcuts import render,redirect
from articles.models import Article
from django.contrib.auth.decorators import login_required 
from .forms import ArticleFormOld,ArticleForm
# Create your views here.



def article_view(request,id):
    article_obj=None
    if id is not None:
        article_obj=Article.objects.get(id=id)
    context={
        "object": article_obj,
    } 

    return render(request,"detail.html",context=context)

@login_required
def article_create_view(request):
    form=ArticleForm(request.POST or None)
    context={
        "form": form
    }
    
    
    if form.is_valid():
              article_object=form.save()
              context['form']=ArticleForm()
            #   title,content=form.cleaned_data.get('title'),form.cleaned_data.get('content')
        # title=request.POST.get("title")
        # content=request.POST.get("content")
      # print(request.POST)
        # print(title,content)
            #   article_object=Article.objects.create(title=title,content=content)
            #   print(article_object.title)
            #   context['object']=article_object
            # #   context['title']=title
            # #   context['content']=content
            #   context['created']=True
    return render(request,"create.html",context=context)

def article_search_view(request):
    query_dict=request.GET
    query=query_dict.get("q")
    article_obj=None
    if query is not None:
        article_obj=Article.objects.get(id=query)

    context={"object":article_obj}
    return render(request,"search.html",context=context)