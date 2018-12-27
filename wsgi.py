# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:55:33 2018

@author: sofyan.fadli
"""

from app import application as _application
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath("/home/sofian/.bashrc"))
sys.path.append(os.path.join(BASE_DIR, '..'))

env_variables_to_pass = ['LD_LIBRARY_PATH', ]

def application(environ, start_response):
    # pass the WSGI environment variables on through to os.environ
    for var in env_variables_to_pass:
        os.environ[var] = environ.get(var, '')
    return _application(environ, start_response)


if __name__ == "__main__":
    application.run(debug=True, threaded=True)    