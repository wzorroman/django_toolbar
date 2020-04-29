import logging
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    var = "wilson"
    logger.error('Mensaje de logger!')
    logger.info("The value of var is %s", var)
    return HttpResponse("Hello, world. You're at the polls index.")

class EjemploView(TemplateView):
    template_name = "ejemploView.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.info('Mensaje de informativo | 20!')
        logger.warning('Mensaje de warning | 30!')
        logger.error('Mensaje de logger | 40!')
        logger.critical('Mensaje critico Nivel | 50!')
        prueba_x = "wilson"
        context.update({
            'var1': prueba_x,
         })
        return context