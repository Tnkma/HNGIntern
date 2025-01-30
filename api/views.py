""" This file is used to create views for the MyInfo app. """
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import pytz

class Info(APIView):
    """ Hardedcoded information about me."""
    def get(self, request):
        """ Returns information about me."""
        datetime = datetime.utcnow().isoformat(timespec="seconds") + "Z"
        data = {
            "email": "onwusilikenonso@gmail.com",
            "current_datetime": datetime,
            "github_url": "https://github.com/Tnkma/HNGIntern"
        }
        return Response(data)