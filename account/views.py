from django.shortcuts import render, redirect
from account.forms import ProfileForm

#def account(request):
#    return render(request, 'account/profile.html')

def account(request):
    error = ''
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была заполнена неверно'

    form = ProfileForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'account/profile.html', context=context)
