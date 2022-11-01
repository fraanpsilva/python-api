
from django.urls import path
from django.contrib import admin
from escolaapi.views import alunos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', alunos)
]