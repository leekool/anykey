#!/bin/sh

# this is no way an ideal way to run the app, but will do for now
if kill $(pgrep -f "python3 app.py"); then
    echo "Existing process killed successfully."
else
    echo "No existing process found."
fi

nohup python3 app.py > /dev/null 2>&1 &
