from django.shortcuts import render
from django.core.mail import send_mail
#from .forms import ContactForm
from .models import Post

def home(request):
    context ={
        "Post": Post.objects.all()
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        v_fullname = request.POST.get('f_fname')
        v_email = request.POST.get('f_email')
        v_message = request.POST.get('f_message')

        # Save the form data to the database
        post = Post(fullname= v_fullname, email= v_email, message= v_message)
        post.save()

        # Send the email
        """
        ///send_mail(
            v_fullname,  # subject
            v_message,  # message
            v_email,  # from email
            ['vshah@gitam.in', 'idkvivinsha@gmail.com'],  # to email
            fail_silently=False  # raise exceptions for sending errors
        )"""


        return render(request, 'contact.html', {'f_fname': v_fullname})
    else:
        return render(request, 'contact.html', {'f_fname' : "vivin"})
