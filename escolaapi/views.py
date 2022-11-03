
from rest_framework import viewsets
from escolaapi.models import Aluno, Curso, Matricula
from escolaapi.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos (as)"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer