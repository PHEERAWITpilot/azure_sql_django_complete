#!/bin/bash
cd /home/site/wwwroot
pip install -r requirements.txt
gunicorn azure_project.wsgi --workers 4 --threads 2 --worker-class sync --bind 0.0.0.0:8000
