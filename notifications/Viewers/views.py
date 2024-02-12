from django.shortcuts import render
from Alerts.models import Notification
from Viewers.models import Viewer
from django.http import JsonResponse


def fetch(request):
    notifications_ = []
    if request.method == 'GET':
        user_id = request.GET['user_id']
        notifications = Notification.objects.exclude(Viewers__viewer_id=user_id)
        for notification in notifications:
            try:
                viewer = Viewer.objects.get(viewer_id=user_id)
            except Viewer.DoesNotExist:
                viewer = Viewer.objects.create(viewer_id=user_id)
            notification.Viewers.add(viewer)
            notifications_.append({'title': notification.Title, 'body': notification.Body})
        data = {
            'notifications': notifications_
        }
        return JsonResponse(data, safe=False)
