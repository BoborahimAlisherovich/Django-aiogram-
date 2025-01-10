from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BotUser, Feedback
from .serializers import BotUserSerializer, FeedbackSerializer


class BotuserApiView(viewsets.ModelViewSet):
    serializer_class = BotUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username:
            return BotUser.objects.filter(username__icontains=username)
        return BotUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put'])
    def update_botuser(self, request, pk=None):
        botuser = self.get_object()
        serializer = self.get_serializer(botuser, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class FeedbackApiView(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        chat_id = self.request.query_params.get('chat_id', None)
        if chat_id:
            return Feedback.objects.filter(bot_user__chat_id=chat_id)
        return Feedback.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put'])
    def update_feedback(self, request, pk=None):
        feedback = self.get_object()
        serializer = self.get_serializer(feedback, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
