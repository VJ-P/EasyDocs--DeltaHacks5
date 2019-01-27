from django.urls import path

from . import views

urlpatterns= [
        path('', views.homepage),
        path('download/zip/<str:filename>', views.downloadzip),
        path('download/docx/<str:filename>', views.downloaddocx)
]
