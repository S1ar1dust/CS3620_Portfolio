from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from BookAPI.models import BookData

def Home(request):
    template = loader.get_template('BookAPI/homePage.html')
    return HttpResponse(template.render({}, request))

def Books(request):
    if 'searchBar' in request.GET:
        searchBar = request.GET['searchBar']
        book_list = BookData.objects.filter(name__icontains=searchBar)
        p = Paginator(book_list, len(book_list))
    else:
        book_list = BookData.objects.all()
        p = Paginator(book_list, 5)
    #book_list = BookData.objects.all()




    # Got quite stuck here at first but used stackoverflow to find a solution. Page link to the solution I used
    # https://stackoverflow.com/questions/66227123/pagenotaninteger-at-products-that-page-number-is-not-an-integer
    page = request.GET.get('page', None)
    if page == None or page == "":
        page = 1
    # or
    if not page:
        page = 1

    books = p.page(page)

    return render(request, 'BookAPI/BooksPage.html', {'book_list': book_list, 'books': books})


    #template = loader.get_template('BookAPI/BooksPage.html')
    #return HttpResponse(template.render({}, request))




