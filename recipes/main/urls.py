from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('recipe/<int:pk>', views.RecipesDetailView.as_view(), name='detail'),
    path('recipe/<int:pk>/update', views.RecipesUpdateView.as_view(), name='update'),
    path('recipe/<int:pk>/delete', views.RecipesDeleteView.as_view(), name='delete'),
]
