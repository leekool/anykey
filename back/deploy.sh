#!/bin/sh

gunicorn_pids=$(pgrep -f "gunicorn")

# kill all existing instances of gunicorn
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

# start gunicorn
gunicorn -w 4 -b "$ANYKEY_URL":5000 --certfile "$CERT_PATH" --keyfile "$KEY_PATH" app:app --daemon
