from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from forms import FormUsuario
from models import Usuario

def lista(request):
    lista_itens =  Usuario.objects.all()
    return render_to_response("lista.html",{'lista_itens':lista_itens})

def item(request,nr_item):
    item = get_object_or_404(Usuario,pk=nr_item)
    if request.method == "POST":
        form = FormUsuario(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return render_to_response("salvo.html",{})
    else:
        form = FormUsuario(instance=item)
    return render_to_response("item.html",{'form':form},context_instance=RequestContext(request))
        
def adiciona(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("salvo.html",{})
    else:
        form = FormUsuario()
    return render_to_response("item.html",{'form':form},context_instance=RequestContext(request))
        