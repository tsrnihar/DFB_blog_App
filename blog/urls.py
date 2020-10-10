from django.urls import path
from .views import BlogListView,BlogDetailView,BlogFormView,BlogUpdateView,BlogDeleteView

urlpatterns = [
    path('blog/',BlogListView.as_view(),name = "blog"),
    path('blog/<int:pk>/',BlogDetailView.as_view(),name = "detail"),
    path('blog/post/',BlogFormView.as_view(),name="create"),
    path('blog/<int:pk>/edit',BlogUpdateView.as_view(),name = "edit"),
    path('blog/<int:pk>/delete',BlogDeleteView.as_view(),name = "delete"),
]
