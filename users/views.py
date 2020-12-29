from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import User,UserContact
from .serializers import UserContactSerializer,UserCreateSerializer,UserFollowingSerializer

class UserContactViewset(viewsets.ViewSet):
    serializer_class = UserContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'

    def create(self,request):
        serializer = UserContactSerializer(data=request.data)
        if serializer.is_valid():
            #user being followed
            to_user = User.objects.get(id=serializer.data['user_to'])
            
            #you cant follow yourself lol
            if self.request.user != to_user:
                try:
                    if serializer.data['action'] == 'follow':
                        UserContact.objects.get_or_create(user_from=self.request.user,user_to=to_user)
                    
                    if serializer.data['action'] == 'unfollow':
                        UserContact.objects.filter(user_from=self.request.user, user_to=to_user).delete() 

                    followers_followings = UserFollowingSerializer(self.request.user)          
                    return Response(followers_followings.data)

                except:
                    return Response({'status':'error'})
            else:
                return Response({'status':'no need to follow yourself'})                    
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    #authenticated user can search for any user's public info
    def retrieve(self, request, username=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset,username=username)
        serializer = UserFollowingSerializer(user)
        return Response(serializer.data)
        