#!/bin/bash

ps -ef | grep /gunicorn |  grep -v  grep | head -1 |awk '{print $2}' | xargs kill -9