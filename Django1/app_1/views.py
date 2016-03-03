from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm #Formulário de criação de usuários
'''
def views_1(request):

#Sem o request no render nao funciona
    return render(request, "templateForm.html")
'''
def views_1(request):
    #Se dados forem passados via POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid(): # se formulario for valido
            form.save() # Cria um novo formulário a partir dos dados passados
            return render(request, 'TemplateForm.html')
        else:
            return render(request, 'templateForm.html', {'form': form})

    # Se nenhum dado for passado, exibe a página de cadastro novamente
    return render(request, 'templateForm.html', {'form': UserCreationForm() })