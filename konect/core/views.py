from django.shortcuts import render, get_object_or_404
from .models import *
from inscrito.models import *
from django.views.generic.edit import CreateView

class Index(CreateView):
    model = Inscricao
    fields = ['nome', 'email']
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['banner'] = Banner.objects.last()
        context['quemsomos'] = QuemSomos.objects.last()
        context['cadastro'] = Cadastro.objects.last()
        return context

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(Index, self).get_form(form_class)
        form.fields['nome'].widget.attrs = {'placeholder': 'Nome Completo'}
        form.fields['email'].widget.attrs = {'placeholder': 'E-mail'}
        return form

def categoria_view(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    areas = Area.objects.filter(categoria=categoria)
    oportunidades = Oportunidade.objects.all()

    context = {
        'categoria' : categoria,
        'areas' : areas,
        'oportunidades' : oportunidades,
    }

    return render(request, 'trabalho-voluntario.html', context)

def area_view(request, slug):
    area = get_object_or_404(Area, slug=slug)
    oportunidades = Oportunidade.objects.filter(area=area)

    context = {
        'area' : area,
        'oportunidades' : oportunidades,
    }

    return render(request, 'empresa-junior.html', context)

def oportunidade_view(request, slug):
    oportunidade = get_object_or_404(Oportunidade, slug=slug)
    area = oportunidade.area
    perguntas = Pergunta.objects.filter(area=area)

    context = {
        'oportunidade' : oportunidade,
        'perguntas' : perguntas,
    }

    return render(request, 'details.html', context)
