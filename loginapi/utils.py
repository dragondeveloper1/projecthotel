# from django import http
# import json

# def Register(request, data):
#     if request.GET.get('debug'):
#         response = json.dumps(data, indent=4)
#         try:
#             from pygments import highlight, lexers, formatters
#             return http.HttpResponse(highlight(response, lexer.get_lexers_by_name('json'),
#             formatters.get_formatter_by_name('html', full=True),
#             ))
#         except ImportError:
#             return http.HttpResponse(response, content_type='text/plain')
#     else:
#         return http.HttpResponse(
#             json.dumps(data), content_type='application/json'
#         )

from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_mail(data):

        email = EmailMessage(subject=data['email_subject'],body=data['email_body'],to=[data['to_email']])
        email.send()

