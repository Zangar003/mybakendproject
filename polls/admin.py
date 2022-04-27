from django.contrib import admin


from .models import Book, Question,  Form_lab, Posts

# Register your models here.

admin.site.register(Question)
admin.site.register(Form_lab)
admin.site.register(Book)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published",)
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Posts, ArticleAdmin)