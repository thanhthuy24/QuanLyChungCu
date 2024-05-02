from django.urls import path, include
from rest_framework import routers
from apartments import views

r = routers.DefaultRouter()

r.register('flats', views.FlatViewSet, 'flats')
r.register('ecabinets', views.ECabinetViewSet, 'ecabinets')
r.register('items', views.ItemViewSet, 'items')
r.register('receipts', views.ReceiptViewSet, 'receipts')
r.register('complaints', views.ComplaintViewSet, 'complaints')
r.register('users', views.UserViewSet, 'users')
r.register('comments', views.CommentViewSet, 'comments')
r.register('surveys', views.SurveyViewSet, 'surveys')
r.register('admins', views.AdminViewSet, 'admins')

urlpatterns = [
    path('', include(r.urls))
]