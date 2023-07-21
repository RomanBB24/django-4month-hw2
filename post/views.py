from datetime import datetime
from django.shortcuts import render
from post.models import Product


def main_page(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def products_views(request):
    if request.method == 'GET':
        product = Product.objects.all()
        context = {
            'product': product
        }
        return render(request, 'products/products.html', context=context)
#
#
# def hello_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Hello its my first project")
#
#
# def now_date(request):
#     if request.method == 'GET':
#         now_time = datetime.now()
#         return HttpResponse(now_time)
#
#
# def goodby_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Goodby user")
