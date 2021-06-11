from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    s = False
    if request.method == 'POST':
        if "contact-form" in request.POST.keys():
            messages = request.POST['contact-name'] + "\n" + \
                       request.POST['contact-email'] + "\n" + \
                       request.POST['contact-message']

            send_mail("CONTACT FORM",
                      messages,
                      settings.EMAIL_HOST_USER,
                      ['support@fast-recovery.org'],
                      fail_silently=False
                      )
            s = True
        elif "send-message" in request.POST.keys():
            messages = request.POST['send-name'] + "\n" + \
                       request.POST['send-email'] + "\n" + \
                       request.POST['send-message']

            send_mail("SEND MESSAGE FORM",
                      messages,
                      settings.EMAIL_HOST_USER,
                      ['support@fast-recovery.org'],
                      fail_silently=False
                      )
            s = True

        else:
            messsages = request.POST["ex-name"] + "\n" + \
                        request.POST["ex-company"] + "\n" + \
                        request.POST["ex-phone"] + "\n" + \
                        request.POST["ex-email"] + "\n" + \
                        request.POST["ex-currency"] + "\n" + \
                        request.POST["ex-amount"] + "\n" + \
                        request.POST["ex-country"] + "\n" + \
                        request.POST["ex-message"]

            send_mail("EXAMINATION FORM",
                      messsages,
                      settings.EMAIL_HOST_USER,
                      ["support@fast-recovery.org"],
                      fail_silently=False
                      )
            s = True

    return render(request, 'home/base.html', {"s": s})


def faq(request):
    context = {
    }
    return render(request, "home/faq.html", context)


def about(request):
    context = {
    }
    return render(request, "home/about.html", context)


def contact(request):

    s = False
    if request.method == 'POST':
        if "contact-form" in request.POST.keys():
            messages = request.POST['contact-name'] + "\n" + \
                       request.POST['contact-email'] + "\n" + \
                       request.POST['contact-message']

            send_mail("CONTACT FORM",
                      messages,
                      settings.EMAIL_HOST_USER,
                      ['support@fast-recovery.org'],
                      fail_silently=False
                      )
            s = True
    return render(request, "home/contact.html", {"s": s})


def privacy(request):
    context = {
    }
    return render(request, "home/privacy.html", context)


def terms(request):
    context = {
    }
    return render(request, "home/terms.html", context)
