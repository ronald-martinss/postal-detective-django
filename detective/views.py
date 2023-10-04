from django.shortcuts import render
from cep_api.client import get_cep
from detective.forms import CepForm
# Create your views here.


def detective_view(request):
    if request.method == "POST":
        form = CepForm(request.POST)
        if form.is_valid():
            uf = form.cleaned_data['uf']
            cidade = form.cleaned_data['cidade']
            logradouro = form.cleaned_data['logradouro']

            response = get_cep(uf, cidade, logradouro)
            return render(request, 'response_view.html', {'response': response})
    else:
        form = CepForm()
    return render(request, 'detective_view.html', {'form': form})
