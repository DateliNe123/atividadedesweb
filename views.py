from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Autor, Livro

class AutorListView(ListView):
    model = Autor

class AutorDetailView(DetailView):
    model = Autor

class AutorCreateView(CreateView):
    model = Autor
    fields = ['nome', 'data_nascimento', 'nacionalidade']
    success_url = reverse_lazy('autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    fields = ['nome', 'data_nascimento', 'nacionalidade']
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor_list')

class LivroListView(ListView):
    model = Livro

class LivroDetailView(DetailView):
    model = Livro

class LivroCreateView(CreateView):
    model = Livro
    fields = ['titulo', 'genero', 'ano_publicacao', 'autor']
    success_url = reverse_lazy('livro_list')

class LivroUpdateView(UpdateView):
    model = Livro
    fields = ['titulo', 'genero', 'ano_publicacao', 'autor']
    success_url = reverse_lazy('livro_list')

class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy('livro_list')
