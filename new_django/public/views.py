from rest_framework.permissions import AllowAny
import requests
from .models import RandomUser
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RandomUserSerializer


class RandomUserViewSet(APIView):
    permission_classes = [AllowAny]
    api_url = 'https://randomuser.me/api/'

    def get(self, request):
        read = RandomUser.objects.all()
        return Response({'posts': RandomUserSerializer(read, many=True).data})

    def post(self, request):
        # Получение данных от API
        response = requests.get(self.api_url)
        info = response.json()

        # Извлечение данных из JSON-ответа
        user_data = info['results'][0]
        user_model_data = {
            "gender": user_data['gender'],
            "first_name": user_data['name']['first'],
            "last_name": user_data['name']['last'],
            "street_number": user_data['location']['street']['number'],
            "street_name": user_data['location']['street']['name'],
            "city": user_data['location']['city'],
            "country": user_data['location']['country'],
            "postcode": user_data['location']['postcode'],
            "login": user_data['login']['username'],
            "password": user_data['login']['password'],
            "born_data": user_data['dob']['date'],
            "age": user_data['dob']['age'],
        }

        serializer = RandomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        random_user = RandomUser.objects.create(**user_model_data)

        return Response({"status": RandomUserSerializer(random_user).data})





