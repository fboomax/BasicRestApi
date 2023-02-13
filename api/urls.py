from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.get_routes),
    path('api/all/', views.article_list),
    path('api/allclass/', views.ArticleAPIView.as_view()),
    path('api/all/<str:pk>/detail/', views.article_detail),
    path('api/all/<str:pk>/detailclass/', views.ArticleAPIDetails.as_view()),
    path('api/all/<str:pk>/update/', views.article_update),
    path('api/all/<str:pk>/delete/', views.article_delete),
    path('api/post/', views.add_article),
]
