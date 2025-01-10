from django.urls import path
from .views import BotuserApiView, FeedbackApiView

botuser_list = BotuserApiView.as_view({'get': 'list', 'post': 'create'})
botuser_detail = BotuserApiView.as_view({'put': 'update_botuser'})

feedback_list = FeedbackApiView.as_view({'get': 'list', 'post': 'create'})
feedback_detail = FeedbackApiView.as_view({'put': 'update_feedback'})

urlpatterns = [
    path('bot-users', botuser_list, name="bot-user-list"),
    path('bot-users/<int:pk>', botuser_detail, name="bot-user-detail"),
    path('feedback', feedback_list, name="feedback-list"),
    path('feedback/<int:pk>', feedback_detail, name="feedback-detail"),
]
