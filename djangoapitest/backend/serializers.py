from django.http import JsonResponse

def GetNames(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')

    if not first_name or not last_name:
        error_message = {'error': 'First name and last name are required.'}
        return JsonResponse(error_message, status=400)
    else:
        name = {'first_name': first_name, 'last_name': last_name}
        return JsonResponse(name)
# URL for Example http://127.0.0.1:8000/getnames/?first_name=Ashish&last_name=Joshi

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Box

@csrf_exempt
def box_detail(request, box_id):
    if request.method == 'GET':
        try:
            box = Box.objects.get(Box_ID=box_id)
            data = {
                'Box_ID': box.Box_ID,
                'Box_material': box.Box_material,
                'QTY_material': box.QTY_material,
            }
            return JsonResponse(data)
        except Box.DoesNotExist:
            return JsonResponse({'error': 'Box not found'}, status=404)
    elif request.method == 'POST':
        try:
            box = Box.objects.get(Box_ID=box_id)
            new_qty = request.GET.get('QTY_material', box.QTY_material)
            if new_qty == box.QTY_material:
                return JsonResponse({'message': 'QTY_material is already up to date'})
            box.QTY_material = new_qty
            box.save(update_fields=['QTY_material'])
            return JsonResponse({'message': 'QTY_material updated successfully'})
        except Box.DoesNotExist:
            return JsonResponse({'error': 'Box not found'}, status=404)
