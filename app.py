# Application 
import os
import pickle
from uuid import uuid1
from flask import Flask, make_response, request
from base64 import b64encode, b64decode
class UserID:
    def __init__(self, uuid=None):
        self.uuid = str(uuid1())
    def __str__(self):
        return self.uuid
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    user_obj = request.cookies.get('uuid')
    if user_obj == None:
        msg = "Seems like you didn't have a cookie. No worries! I'll set one now!"
        response = make_response(msg)
        user_obj = UserID()
        response.set_cookie('uuid', b64encode(pickle.dumps(user_obj)))
        return response
    else:
        return "Hey there! {}!".format(pickle.loads(b64decode(user_obj)))
if __name__ == "__main__":
    app.run(host='0.0.0.0')