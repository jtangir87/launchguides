from django.shortcuts import render
from django.template.loader import get_template
from django.http import JsonResponse
from django.core.mail import send_mail

# Create your views here.

def contact_us(request):
    data = dict()
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        template = get_template('pages/contact_us.txt')
        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message,
        }
        content = template.render(context)
        send_mail(
            "Launch Guides Contact Us",
            content,
            "{}<{}>".format(name, email),
            ['info@mylaunchguides.com'],
            fail_silently=False,
        )
        data["form_is_valid"] = True
    else:
        data["form_is_valid"] = False
    return JsonResponse(data)


def subscribe(request):
    data = dict()
    if request.method == "POST":
        email = request.POST.get('email')

        template = get_template('pages/subscribe.txt')
        context = {
            'email': email,
        }
        content = template.render(context)
        send_mail(
            "Launch Guides Subscribe",
            content,
            email,
            ['info@mylaunchguides.com'],
            fail_silently=False,
        )
        data["form_is_valid"] = True
    else:
        data["form_is_valid"] = False
    return JsonResponse(data)