# -*- coding: utf-8 -*-

import os
import sys

from flask import Flask

def add_path():
    global project_root
    file_path = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.abspath("%s/../" % file_path)
    sys.path.insert(0, project_root)
    return project_root

project_root = add_path()

def import_folder(folder_name, base_path = None):
    full_path = os.path.join(base_path, folder_name)
    folder = os.path.abspath(full_path)
    sys.path.insert(0, folder)


import_folder(folder_name='trote_game', base_path=project_root)

app = Flask(__name__)
app.config.from_pyfile('app.cfg')

for key in app.config.keys():
    if os.environ.has_key(key):
        type_of_config = type(app.config[key])
        if type_of_config is bool:
            if os.environ[key] == "False":
                app.config[key] = False
            else:
                app.config[key] = True
        elif type_of_config is int:
            app.config[key] = int(os.environ[key])
        else:
            app.config[key] = os.environ[key]

def get_app():
    return app

