import requests
from requests.auth import HTTPBasicAuth
from rest_framework.authtoken.models import Token

url = "http://127.0.0.1:8000/routercity/"

token = Token.objects.create(user='Erhan')