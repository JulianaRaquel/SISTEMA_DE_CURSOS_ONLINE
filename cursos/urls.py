
from django.urls import path
from cursos.views import home, curso, aula, comentarios


urlpatterns = [
    path('', home, name='home'),
    path('curso/<int:id>', curso, name='curso'),
    path('aula/<int:id>', aula, name='aula'),
    path('comentarios/', comentarios, name='comentarios'),
]