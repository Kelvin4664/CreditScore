from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .utils import credit_score

class IndexView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, username):

        requested_user = get_object_or_404(User, username=username)

        score, risk_level = credit_score(requested_user)

        content = {'user': requested_user.username,
                   'score':score,
                   'risk_level':risk_level }

        return Response(content)