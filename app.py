# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:38:08 2018

@author: sofyan.fadli
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# from security import authenticate, identity
from sim import Sim
from ktp import Ktp

application = Flask(__name__)
application.secret_key = 'jose'
api = Api(application)

# jwt = JWT(application, authenticate, identity) # auth
    
api.add_resource(Sim, '/sim')
api.add_resource(Ktp, '/ktp')

if __name__ == '__main__':
    # application.run(host='0.0.0.0', port=5000, debug=True)
    application.run(host='0.0.0.0' ,debug=True)
