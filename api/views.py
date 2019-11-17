# encoding=utf8
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from dotenv import load_dotenv
import json
import ast
import os
import requests
from django.http import HttpResponse



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=BASE_DIR)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_word(request):
    """
    get word from TDK
    """

    try:
        data = json.loads( request.body.decode('utf-8') )
    except KeyError:
      Response("Malformed data!")

    try:
        # ast.literal_eval(data["meaning"])
        # ast.literal_eval(data["adage"])
        
        base_url = os.getenv('TDK_API_URL')
        params = {"ara":data["word"]}
        response = requests.get(base_url, params=params)
        response.encoding = "utf-8"
        response_data = response.text
        response_data = response.text[1:-1]
        response_data = json.loads(response_data)

        result = {}
        if 'atasozu' in response_data:
            try:
                if ast.literal_eval(data["atasozu"]) is True :
                        atasozu_list = []
                        for atasozu in response_data["atasozu"]:
                            atasozu_list.append(atasozu["madde"])
                        result["atasozu"] = atasozu_list
            except ValueError:
                pass

        if 'anlamlarListe' in response_data:
            try:
                if ast.literal_eval(data["anlam"]) is True:
                    anlam_list = []
                    for anlam in response_data["anlamlarListe"]:
                        anlam_list.append(anlam["anlam"])
                        print(anlam)
                    result["anlam"] = anlam_list
            except ValueError:
                pass
            
        return Response(result)
    # todo: JSONDecodeError hatasi düzeltilecek (coklu json calisması)
    except json.decoder.JSONDecodeError as e:
        return HttpResponse("JSONDecodeError" , status=500)

    except Exception as e:
        raise e
        return Response("Try Again!")