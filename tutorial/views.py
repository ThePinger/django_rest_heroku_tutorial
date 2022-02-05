from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from tutorial.models import Tutorial
from tutorial.serializers import TutorialSerializer

class TutorialsView(APIView):

    def get(self, request):
        tutorials = Tutorial.objects.all()
        serialized_tutorials = TutorialSerializer(tutorials)
        return Response(data=serialized_tutorials.data, status=status.HTTP_200_OK)