from django.urls import path, include
from rest_framework import routers
from apartments import views

r = routers.DefaultRouter()

r.register('flats', views.FlatViewSet, 'flats')
r.register('ecabinets', views.ECabinetViewSet, 'ecabinets')
r.register('items', views.ItemViewSet, 'items')
r.register('receipts', views.ReceiptViewSet, 'receipts')

r.register('complaints', views.ComplaintViewSet, 'complaints')
r.register('addcomplaints', views.AddComplaintViewSet, 'addcomplaints')

r.register('users', views.UserViewSet, 'users')
r.register('comments', views.CommentViewSet, 'comments')
# r.register('survey', views.SurveysViewSet, 'survey')
r.register('carcards', views.CarCardViewSet, 'carcards')
r.register('tags', views.TagViewSet, 'tags')

r.register('surveys', views.SurveyViewSet, 'surveys')
r.register('questions', views.QuestionViewSet, 'questions')
r.register('choices', views.ChoiceViewSet, 'choices')
r.register('answers', views.AnswerViewSet, 'answers')

urlpatterns = [
    path('', include(r.urls)),
    # path('save-token/', views.save_token, name='save_token'),
    # path('send-notification/', views.send_notification, name='send_notification'),
]