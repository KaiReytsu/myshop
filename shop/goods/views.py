from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Storage
from .serializers import StorageSerializer
import json

def product_view(request):
    
    if str(request.method).lower() == 'post':
        if 'productname' in request.POST.keys():
            content = request.POST
        else:
            data = request.body.decode('utf-8')
            content = json.loads(data)
        product = Product(
            product_name=content['productname'], 
            price=content['price'])
        product.save()
        storage = Storage(
            product_id=product.id, 
            stock=content['stock'])
        storage.save()

    return render(request, 'goods.html')

def storage_view(request):
    storage = Storage.objects.all()
    num_pages = (len(storage) // 5)
    if len(storage) % 5 > 0:
        num_pages +=1
    if str(request.method).lower() == 'post':
        data = request.body.decode('utf-8')
        content = json.loads(data)
        content_range = content['page']
        high_element = content_range * 5
        low_element = high_element - 5
        storage = storage[low_element:high_element]
        serial_item = []
        for item in storage:
            serial_item.append(StorageSerializer(item).data)
        return JsonResponse({'storage': serial_item})
    return render(request, 'storage.html', {'num_pages': num_pages})