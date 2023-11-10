from django.shortcuts import render, redirect
from .models import Statementes
from .forms import StatementsForm
from django.views.generic import DeleteView, UpdateView

def index(request):
    tasks = Statementes.objects.all
    return render(request, 'main/index.html', {'title': 'Главная страница',
                                               'tasks': tasks})

def statementes(request):
    error = ""
    if request.method == 'POST':
        form = StatementsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = StatementsForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/statementes.html', context)

class StatementesDeleteView(DeleteView):
    model = Statementes
    success_url = '/'
    template_name = 'main/task-delete.html'

class StatementesUpdateView(UpdateView):
    model = Statementes
    template_name = 'main/create.html'
    form_class=StatementsForm
    success_url = '/'