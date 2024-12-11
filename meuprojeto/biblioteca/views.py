from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Autor, Livro

# Views para Autor
class AutorListView(ListView):
    model = Autor
    template_name = 'autor_list.html'

class AutorCreateView(CreateView):
    model = Autor
    fields = ['nome', 'data_nascimento']
    template_name = 'autor_form.html'
    success_url = reverse_lazy('autor-list')

class AutorUpdateView(UpdateView):
    model = Autor
    fields = ['nome', 'data_nascimento']
    template_name = 'autor_form.html'
    success_url = reverse_lazy('autor-list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autor_confirm_delete.html'
    success_url = reverse_lazy('autor-list')

# Views para Livro
class LivroListView(ListView):
    model = Livro
    template_name = 'livro_list.html'

class LivroCreateView(CreateView):
    model = Livro
    fields = ['titulo', 'autor', 'publicado_em']
    template_name = 'livro_form.html'
    success_url = reverse_lazy('livro-list')

class LivroUpdateView(UpdateView):
    model = Livro
    fields = ['titulo', 'autor', 'publicado_em']
    template_name = 'livro_form.html'
    success_url = reverse_lazy('livro-list')

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'livro_confirm_delete.html'
    success_url = reverse_lazy('livro-list')

