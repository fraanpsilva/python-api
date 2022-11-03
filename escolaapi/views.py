
from rest_framework import viewsets
from escolaapi.models import Aluno, Curso
from escolaapi.serializer import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos (as)"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer