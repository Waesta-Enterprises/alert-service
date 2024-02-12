from django.http import JsonResponse
from .models import Notification
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def recieve(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Notification.objects.create(
            Title=title,
            Body=body
        )
        return JsonResponse({'message': 'created'})

