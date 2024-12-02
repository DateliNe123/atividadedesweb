from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor_detail'),
    path('autores/criar/', views.AutorCreateView.as_view(), name='autor_create'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor_edit'),
    path('autores/<int:pk>/deletar/', views.AutorDeleteView.as_view(), name='autor_delete'),
    
    path('livros/', views.LivroListView.as_view(), name='livro_list'),
    path('livros/<int:pk>/', views.LivroDetailView.as_view(), name='livro_detail'),
    path('livros/criar/', views.LivroCreateView.as_view(), name='livro_create'),
    path('livros/<int:pk>/editar/', views.LivroUpdateView.as_view(), name='livro_edit'),
    path('livros/<int:pk>/deletar/', views.LivroDeleteView.as_view(), name='livro_delete'),
]
