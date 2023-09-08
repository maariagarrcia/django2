from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    # 1 crear la planttilla vacia
    contact_form = ContactForm()

    if request.method == "POST":
        # si se ha llenado el formulario
        contact_form = ContactForm(data=request.POST)
        # comprobar si es valido el formulario es decir todoo lo que se ha llenado sea  correcto
        
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            # enviar correo y redireccionar
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                " no-contestar@inbox_maltrap.io",
                ["mrrmn@myuax.com"],
                reply_to=[email] 
            )
            
            try:
                email.send()
                # todo ha ido bien
                return redirect(reverse('contact')+"?ok")
            except:
                # algo no ha ido bien
                return redirect(reverse('contact')+"?fail")
            
            
            

        

    return render(request,"contact/contact.html",{'form':contact_form})

