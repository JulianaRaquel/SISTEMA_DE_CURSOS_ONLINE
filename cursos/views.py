from django.http import HttpResponse
from django.shortcuts import redirect, render
from cursos.models import Cursos, Aulas, Comentarios
import json


def home(request):
    if request.session.get('usuario'):
        cursos = Cursos.objects.all()
        request_usuario = request.session.get('usuario')
        return render(request, 'home.html', {'cursos': cursos, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')


def curso(request, id):
    if request.session.get('usuario'):
        aulas = Aulas.objects.filter(curso=id)
        request_usuario = request.session.get('usuario')
        return render(request, 'curso.html', {'aulas': aulas, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')

def aula(request, id):
    if request.session.get('usuario'):
        aula = Aulas.objects.get(id=id)
        comentarios = Comentarios.objects.filter(aula=id).order_by('-data')
        return render(request, 'aula.html', {'aula': aula, 'usuario_id': request.session.get('usuario'), 'comentarios': comentarios})
    else:
        return redirect('/auth/login/?status=2')


def comentarios(request):
    usuario_id = int(request.POST.get('usuario_id'))
    comentario = request.POST.get('comentario')
    aula_id = int(request.POST.get('aula_id'))

    comentario_instancia = Comentarios(usuario_id=usuario_id,
                                       comentario=comentario,
                                       aula_id=aula_id)
    comentario_instancia.save()

    comentarios = Comentarios.objects.filter(aula=aula_id).order_by('-data')
    somente_nomes = [i.usuario.nome for i in comentarios]
    somente_comentarios = [i.comentario for i in comentarios]
    comentarios = list(zip(somente_nomes, somente_comentarios))

    return HttpResponse(json.dumps({'status': '1', 'comentarios': comentarios}))


