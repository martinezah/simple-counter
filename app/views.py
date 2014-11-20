import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import Counter

@csrf_exempt
def index(request, id):
    if request.method == 'PUT':
        counter, created = Counter.objects.get_or_create(id=id)
        counter.value = 0
        counter.step = 1000
        counter.save()
        response = counter.value
    if request.method == 'GET':
        counter = Counter.objects.get(id=id)
        response = counter.value
    if request.method == 'POST':
        counter = Counter.objects.get(id=id)
        counter.value += counter.step
        counter.save()
        response = counter.value
    if request.method == 'DELETE':
        counter = Counter.objects.get(id=id)
        counter.delete()
        response = None
    return HttpResponse(json.dumps(response), content_type="application/json")
