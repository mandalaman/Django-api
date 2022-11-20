from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page")
    friend = [
        'rave',
        'asham',
        'slkd'
    ]
    return JsonResponse(friend, safe=False)
