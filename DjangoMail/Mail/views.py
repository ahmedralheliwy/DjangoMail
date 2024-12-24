from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import MailForm

def mail(request):
    context = {}

    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data['to']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [to],
                    fail_silently=False,
                )
                context['success'] = 'Email sent successfully.'
            except Exception as e:
                context['error'] = f'Error Sending Email: {e}'
    else:
        form = MailForm()

    context['form'] = form
    return render(request, 'mail.html', context)
