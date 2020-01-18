from django.contrib import admin
from news.models import News, Category #absolute import..best practice

# Register your models here.
# admin.site.register(News)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at","cover_image")
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("author",)
    # raw_id_fields = ("category",)

admin.site.register(Category)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ("title")
