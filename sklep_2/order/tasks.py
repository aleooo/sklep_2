from io import BytesIO

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

from .models import Order

# @shared_task
# def order_pdf(base_url, order_id):
#     object_order = Order.objects.get(id=order_id)
#     names_products = 'You ordered: ' + ',  '.join([product.product.name for product in object_order.products.all()])
#     email = EmailMessage(subject=names_products, from_email=settings.EMAIL_HOST_USER, to=[object_order.email])
#     html = render_to_string('content/order/pdf.html', {'order': object_order})
#     out = BytesIO()
#     #Must add STATIC_ROOT and make collectstatic in development
#     weasyprint.HTML(string=html, base_url=base_url).write_pdf(out)
#     email.attach( f'order_{object_order.id }.pdf', out.getvalue(), 'application/pdf')
#     email.send()
#     return "success" 

@shared_task
def order_pdf(order_id):
    object_order = Order.objects.get(id=order_id)
    names_products = 'You ordered: ' + ',  '.join([product.product.name for product in object_order.products.all()])
    html = render_to_string('content/order/pdf.html', {'order': object_order})
    email = EmailMultiAlternatives(subject=names_products, from_email=settings.EMAIL_HOST_USER, to=[object_order.email])
    email.attach_alternative(html, 'text/html')
    email.send()
    return(f'send email to {object_order.email}')

