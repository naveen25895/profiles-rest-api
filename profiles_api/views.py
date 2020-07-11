from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView feature"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, delte',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello!', 'an_appview':an_apiview})
