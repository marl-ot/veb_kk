from django.shortcuts import render, redirect
from ratings.models import Articles
from ratings.forms import ArticlesForm
from django.views.generic import DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

def ratings(request):
    estimation= Articles.objects.order_by('surname')
    return render(request, 'table/table_rating.html', {'estimation':estimation})


class StudentsDetailView(DetailView):
    model = Articles
    template_name = 'table/details_view.html'
    context_object_name = 'article'


class StudentsUpdateView(UpdateView):
    model = Articles
    template_name = 'table/table_editing.html'
    form_class = ArticlesForm

    def get_success_url(self):
        return reverse_lazy('ratings')
    


class StudentsDeleteView(DeleteView):
    model = Articles
    success_url = 'ratings'
    template_name = 'table/table_delete.html'

    def get_success_url(self):
        return reverse_lazy('ratings')


def editing(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ratings')
        else:
            error = 'Форма была заполнена неверно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'table/table_editing.html', data)
