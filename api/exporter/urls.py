from django.urls import path
from .views import CategoryView, ExporterView, ExporterDetailView

urlpatterns = [
    path('/categories', CategoryView.as_view()),
    path('', ExporterView.as_view()),
    path('/<int:exporter_id>', ExporterDetailView.as_view()),
]