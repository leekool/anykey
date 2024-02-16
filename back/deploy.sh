#!/bin/sh

# this is no way an ideal way to run the app, but will do for now
if kill $(pgrep -f "python3 app.py"); then
    echo "Existing process killed successfully."
else
    echo "No existing process found."
fi

# nohup python3 app.py > /dev/null 2>&1 &
gunicorn -w 4 -b 0:0:0:0:5000 --certfile "$CERT_PATH" --keyfile "$KEY_PATH" app:app &
