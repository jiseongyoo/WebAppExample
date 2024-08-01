from flask import jsonify
import requests
import json

class Test:
    def run(self, request):
        params = request.get_json()
        print("받은 Json 데이터 ", params)

        self.post(request)

        response = {
            "result": "test"
        }

        return jsonify(response)

    def post(self, request):
        url = "http://127.0.0.1:8000/third"
        headers = {"Content-Type": "application/json"}
        temp = request.get_json()
        data = json.dumps(temp)

        response = requests.post(url, headers=headers, data=data)
        print("response: " , response)
        print("response.text: ", response.text)
