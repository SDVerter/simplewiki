from django.shortcuts import render

# Create your views here.




from django.shortcuts import redirect

# Create your views here.

from django.contrib.postgres.search import SearchQuery,  SearchVector
from .models import Page

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects

    if Page.objects.filter(url=request.get_full_path()).count() >0:
          content=  list(Page.objects.filter(url=request.get_full_path()))[0].text_rendered
    else:
        content= "/admin/main/page/add/?url=" +request.get_full_path()
        return redirect(content)
    

    context = {
        'content': content,   
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def search(request):

#content =Page.objects.filter(text_rendered__search=)

    vector = SearchVector('text_rendered', config='english') 


    q= request.GET.get("q").split(" ")
    q= ' & '.join(q)
    query = SearchQuery(q, search_type="phrase")
    content ="no"
    url =""
    if Page.objects.annotate(search=vector).filter(search=query).count() >0: 
        content = list(Page.objects.annotate(search=vector).filter(search=query))
        



    context = {
        "url" : url,
        'content': content,   
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'search.html', context=context)

