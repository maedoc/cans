from django.http import JsonResponse

def github(request, **kwds):
    data = {}
    data.update(kwds)
    data.update({'request': repr(request)})
    return JsonResponse(data)
