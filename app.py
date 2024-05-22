#!/usr/bin/env python
# Author: Ryan Tiffany
# Copyright (c) 2024
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__author__ = 'ryantiffany'

import os
import socket
from datetime import datetime 
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

"""
declare flask app
"""
app = Flask(__name__)
Bootstrap(app)

"""declare route for app"""
@app.route('/')
def home():
    app_version = os.getenv('K_REVISION')
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    message = "Welcome to the demo app!."
    items = [
        {'title': 'App Revision', 'content': app_version },
        {'title': 'Container Message', 'content': message },
        {'title': 'Container IP Address', 'content': ip_address },
        {'title': 'Container Hostname', 'content': hostname }
    ]
    return render_template('index.html', items=items)
"""invoke script"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

