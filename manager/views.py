from django.contrib.auth.models import User, Group
from django.db.models import F
from django.http import request
from rest_framework import viewsets, status, generics
from rest_framework import permissions
from rest_framework.response import Response

from manager.models import Transaction, UserProfile
from manager.serializer import UserSerializer, GroupSerializer, TransactionSerializer


from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)


class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.create()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            queryset_profile = UserProfile.objects.get(user_id=request.user.pk)
            queryset_profile.balance = queryset_profile.balance - float(request.data['amount'])
            queryset_profile.save(update_fields=['balance'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TransactionSortList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'amount', 'time']