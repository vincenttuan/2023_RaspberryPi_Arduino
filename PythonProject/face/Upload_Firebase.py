import requests
import json

def change_face_id(msg):
    firebase_url = 'https://iotfb-fc0b9.firebaseio.com/'
    data = {'faceid':msg}
    result = requests.put(firebase_url + '/opencv.json', verify=True, data=json.dumps(data))
    print(result)


if __name__ == '__main__':
    change_face_id('ok')
