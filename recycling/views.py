from django.http import JsonResponse

def products(request):
    if request.method == 'GET':
        
        return JsonResponse()