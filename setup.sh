#!/usr/bin/env bash

chmod +x xcode_runner.py
OLD_FILE=/usr/local/bin/xcode_runner

if [ -f "$FILE" ]; then
    rm OLD_FILE
fi

cp -f xcode_runner.py /usr/local/bin/xrun
