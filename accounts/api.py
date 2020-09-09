from rest_framework import generics, permissions, status
from rest_framework.response import Response
from knox.models import AuthToken
from accounts.serializers import UserGetSerializer, RegisterSerializer, LoginSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from accounts.models import *
from maps.serializers import *

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserGetSerializer(
                user, context=self.get_serializer_context()
            ).data,
            "token": token
        })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserGetSerializer(
                user, context=self.get_serializer_context()
            ).data,
            "token": token
        })

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserGetSerializer

    def get_object(self):
        return self.request.user


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserGetSerializer

    def get_object(self):
        return self.request.user


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def send_friend_request(request, *args, **kwargs):
    user_id = request.data.get('user_id')
    friend_email = request.data.get('email')

    try:
        from_user= User.objects.get(id=user_id)
        to_user = User.objects.get(email=friend_email)
        FriendRequest.objects.create(from_user=from_user, to_user=to_user)
    except ObjectDoesNotExist as err:
        print(err)
        return Response({'detail': 'User with provided email not found'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response({'detail': 'Request already sent to user'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': f'You have shared with {to_user.first_name}'}, status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def accept_friend_request(request, *args, **kwargs):
    user_id = request.data.get('user_id')
    friend_id = request.data.get('friend_id')

    try:
        from_user= User.objects.get(id=friend_id)
        to_user = User.objects.get(id=user_id)

        friends = Friends.objects.create()
        friends.users.add(from_user, to_user)
        # add friend
        request = FriendRequest.objects.get(from_user=from_user, to_user=to_user)
        # delete
        request.delete()
    except ObjectDoesNotExist as err:
        print(err)
        return Response({'detail': 'User with provided email not found'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': f'You have shared with '}, status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_friends_locations_list(request, *args, **kwargs):
    friends_list = []
    user=request.user

    try:
        for friend in User.objects.filter(friends_set__users__id=user.id).exclude(id=user.id):
            friends_list = friends_list + (LocationSerializer(friend.locations.all(), many=True).data)
    except Exception as err:
        print(err)
        return Response({'detail': 'Something Went Wrong'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(friends_list, status.HTTP_201_CREATED)
