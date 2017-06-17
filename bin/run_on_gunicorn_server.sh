#!/bin/bash

LANG=zh_CN.UTF-8

function get_gunicorn_dir(){
    start_script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    gunicorn_dir=$start_script_dir/../stone_rest_python_pkg/bin
}

function get_gunicorn_conf(){
    gunicorn_conf=$start_script_dir/../conf/gunicorn.py
}

function get_wsgi_module_dir(){
    wsgi_module_dir=$start_script_dir/../src
}

function run_on_gunicorn(){
    cd $wsgi_module_dir && nohup $gunicorn_dir/gunicorn -c $gunicorn_conf wsgi:gunicorn_application &
}

get_gunicorn_dir
get_gunicorn_conf
get_wsgi_module_dir
run_on_gunicorn


