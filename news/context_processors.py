from django.shortcuts import render
from news.models import Category  #absolute import


def categories(request):
    category_list = Category.objects.all()
    return {"categories": category_list}

    # 5 features in admin