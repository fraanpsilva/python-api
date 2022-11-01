from django.contrib import admin
from escolaapi.models import Aluno, Curso

# configurando 
class Alunos(admin.ModelAdmin):
    list_display: ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links: ('id', 'nome') # caso eu quiser fazer alguma alteração, posso clicar em uma dessas opções
    search_fields: ('nome', ) # quando eu quiser fazer alguma busca, busco pelo nome
    list_per_page: 20 # paginação
    
# registrando essa configuração
admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
   list_display: ('id', 'codigo_curso', 'descricao') 
   list_display_links: ('id', 'codigo_curso')
   search_fields: ('codigo_curso', )
   list_per_page: 20 # paginação 
   
# registrando essa configuração
admin.site.register(Curso, Cursos)