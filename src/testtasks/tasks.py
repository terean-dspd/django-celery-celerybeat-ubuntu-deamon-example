from __future__ import absolute_import, unicode_literals
from celery.decorators import task

@task(name="celery_print_task") #makes the function celery task with explicit name
def celerypt(str):
    return str
