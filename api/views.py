""" This file is used to create views for the MyInfo app. """
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import pytz

class Info(APIView):
    """ Hardedcoded information about me."""
    def get(self, request):
        """ Returns information about me."""
        data = {
            "email": "onwusilikenonso@gmail.com",
            "current_datetime": datetime.now(pytz.utc).replace(microsecond=0).isoformat() + "Z",
            "github_url": "https://github.com/Tnkma/HNGIntern"
        }
        return Response(data)