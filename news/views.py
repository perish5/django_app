from django.shortcuts import render, get_object_or_404 # used to aviod server down
from django.views import View
from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView ,ListView, DetailView
from news.models import Category, News

class CategoryNewsView(View):
    def get(self, request,category_id, *args, **kwargs):
        template_name = "news/categories.html"
        #category = Category.object.get(pk=category_id)  if id =100 and if there is no object in server, it causes server down so we use get_object_or_404
        category = get_object_or_404(Category,pk=category_id)
        category_news_list = News.objects.filter(category=category)
        return render(request,template_name,{"category_news_list":category_news_list, "category":category})



   # class CategoryNewsView(ListView):
#     model = News
#     context_object_name = "category_news_list"
#     template_name = "news/categories.html"

#     # queryset = News.objects.all()

#     def get_queryset(self):
#         print("KWARGS: ", self.kwargs)
#         category_id = self.kwargs["category_id"]
#         category = get_object_or_404(Category, id=category_id)
#         return News.objects.filter(category=category)
# 
#      


# front page ko trending news haru ma latest news dekhauna and dynamic banauna
class NewsTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        print(categories)
        category_news_list = {}
        for category in categories:
            # context[category.title] = News.objects.filter(category=category)
            category_news_list[category] = News.objects.filter(category=category)
        context["news_list"] = News.objects.all().order_by("-created_at")[:4] # - le last ma added latest news haru dekhaua first ma
        context["trending_news"] = News.objects.order_by("-count")
        context["category_news_list"] = category_news_list
        print(context)
        return context

# news ma click garesi single news matra auna ko lagi
class NewsDetail(DetailView):
    model = News
    template_name = "news/single_news.html"
    context_object_name = "detail_news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1  # to count views
        self.object.save()
        context["popular_news"] = News.objects.order_by("-count")[:4]
        return context