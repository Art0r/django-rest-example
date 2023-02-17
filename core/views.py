from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user-retrieve': reverse('user-retrieve', request=request, format=format),
        'user-create': reverse('user-create', request=request, format=format),
        'account': reverse('account-list', request=request, format=format)
    })