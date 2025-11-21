from django.urls import path
from .views import (
    ViniloListView,
    ViniloDetailView,
    ViniloCreateView,
    ViniloUpdateView,
    ViniloDeleteView
)

urlpatterns = [
    path('', ViniloListView.as_view(), name='vinilo-list'),
    path('vinilo/<int:pk>/', ViniloDetailView.as_view(), name='vinilo-detail'),
    path('vinilo/crear/', ViniloCreateView.as_view(), name='vinilo-create'),
    path('vinilo/<int:pk>/editar/', ViniloUpdateView.as_view(), name='vinilo-update'),
    path('vinilo/<int:pk>/eliminar/', ViniloDeleteView.as_view(), name='vinilo-delete'),
]


