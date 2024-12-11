from django.urls import path
from . import views

urlpatterns = [
    # URLs para Autor
    path('autores/', views.AutorListView.as_view(), name='autor-list'),
    path('autores/novo/', views.AutorCreateView.as_view(), name='autor-create'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor-update'),
    path('autores/<int:pk>/deletar/', views.AutorDeleteView.as_view(), name='autor-delete'),
    
    # URLs para Livro
    path('livros/', views.LivroListView.as_view(), name='livro-list'),
    path('livros/novo/', views.LivroCreateView.as_view(), name='livro-create'),
    path('livros/<int:pk>/editar/', views.LivroUpdateView.as_view(), name='livro-update'),
    path('livros/<int:pk>/deletar/', views.LivroDeleteView.as_view(), name='livro-delete'),
]
