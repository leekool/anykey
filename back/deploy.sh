#!/bin/sh

# if kill $(pgrep -f "python3 app.py"); then
#     echo "Existing process killed successfully."
# else
#     echo "No existing process found."
# fi
#
# nohup python3 app.py > /dev/null 2>&1 &

gunicorn_pids=$(pgrep -f "gunicorn")

if [ -n "$gunicorn_pids" ]; then
    for pid in $gunicorn_pids; do
        if kill "$pid"; then
            echo "gunicorn process $pid killed"
        else
            echo "failed to kill gunicorn process $pid"
        fi
    done
else
    echo "no existing gunicorn processes found"
fi

gunicorn -w 4 -b "$ANYKEY_URL":5000 --certfile "$CERT_PATH" --keyfile "$KEY_PATH" app:app --daemon
