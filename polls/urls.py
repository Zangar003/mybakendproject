from django.urls import path
from .models import Book
from .forms import BookCreate
from . import views
from .views import ArticleListView, ArticleDetailView

from startproject.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path('base/', views.base, name ="result") ,
    path('add/',views.addpage, name ="add_page"),
    path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),  # new
    path("slug/", ArticleListView.as_view(), name="article_list"),
    path('gmail/', views.sendMail, name ="gmail"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
]
#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)