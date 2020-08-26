from rest_framework.response import Response
from rest_framework.views import APIView
from user_app.models import ApiUser
from .serializers import LoggedInUserSerializer

class OnlineUserListView(APIView):

    def get(self, request):
        logged_in_users = ApiUser.objects.filter(logged_status=ApiUser.LOGGED_IN).exclude(username=request.user.username)
        logged_in_users = LoggedInUserSerializer(logged_in_users, many=True).data
        return Response(logged_in_users)

