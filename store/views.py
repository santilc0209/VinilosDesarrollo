from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vinilo

class ViniloListView(ListView):
    model = Vinilo
    template_name = "store/vinilo_list.html"
    context_object_name = "vinilos"

class ViniloDetailView(DetailView):
    model = Vinilo
    template_name = "store/vinilo_detail.html"
    context_object_name = "vinilo"

class ViniloCreateView(CreateView):
    model = Vinilo
    template_name = "store/vinilo_form.html"
    fields = ['titulo', 'artista', 'año', 'precio', 'stock', 'proveedor', 'canciones']
    success_url = reverse_lazy('vinilo-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear Vinilo"
        return context

class ViniloUpdateView(UpdateView):
    model = Vinilo
    template_name = "store/vinilo_form.html"
    fields = ['titulo', 'artista', 'año', 'precio', 'stock', 'proveedor', 'canciones']
    success_url = reverse_lazy('vinilo-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar Vinilo"
        return context

class ViniloDeleteView(DeleteView):
    model = Vinilo
    template_name = "store/vinilo_confirm_delete.html"
    success_url = reverse_lazy('vinilo-list')
