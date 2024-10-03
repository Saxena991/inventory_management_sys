from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserItem
from .serializers import ItemSerializer
from rest_framework.response import Response
from django.core.cache import cache

class ItemViewSet(viewsets.ModelViewSet):
    queryset = UserItem.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs['pk']
        cached_item = cache.get(item_id)
        if cached_item:
            return Response(cached_item)
        else:
            response = super().retrieve(request, *args, **kwargs)
            cache.set(item_id, response.data, timeout=300)  # cache for 5 minutes
            return response












































