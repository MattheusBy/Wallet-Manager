from django.urls import include, path
from rest_framework import routers

from manager import views
from manager.views import TransactionView, TransactionCreateView,TransactionSortList

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('transaction/', TransactionView.as_view()),
    path('transaction_create/', TransactionCreateView.as_view()),
    path('transaction_sort/', TransactionSortList.as_view()),
]
