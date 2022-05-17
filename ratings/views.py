from django.shortcuts import render, redirect
from ratings.models import Articles
from main.views import pageNotFound
from ratings.forms import ArticlesForm
from django.views.generic import DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

def ratings(request):
    estimation= Articles.objects.order_by('surname')
    if request.user.is_teacher:
        return render(request, 'ratings/table_rating.html', {'estimation':estimation})
    else:
        return pageNotFound(request)


class StudentsDetailView(DetailView):
    model = Articles
    template_name = 'ratings/details_view.html'
    context_object_name = 'article'


class StudentsUpdateView(UpdateView):
    model = Articles
    template_name = 'ratings/table_editing.html'
    form_class = ArticlesForm

    def get_success_url(self):
        return reverse_lazy('ratings')
    


class StudentsDeleteView(DeleteView):
    model = Articles
    success_url = 'ratings'
    template_name = 'ratings/table_delete.html'

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

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'ratings/table_editing.html', context=context)
