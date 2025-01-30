""" This file is used to create views for the MyInfo app. """
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import pytz

class Info(APIView):
    """ Hardedcoded information about me."""
    def get(self, request):
        """ Returns information about me."""
        date_time = datetime.utcnow().isoformat(timespec="seconds") + "Z"
        data = {
            "email": "onwusilikenonso@gmail.com",
            "current_datetime": date_time,
            "github_url": "https://github.com/Tnkma/HNGIntern"
        }
        return Response(data)