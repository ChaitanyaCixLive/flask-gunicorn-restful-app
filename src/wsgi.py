#! -*- coding=utf-8 -*-


import controller.all_rest_api as api_controller
import eventlet
import sys,logging
eventlet.monkey_patch()


def create_app():
  # 设置日志
  looger_handler()
  # 这个工厂方法可以从你的原有的 `__init__.py` 或者其它地方引入。
  app = api_controller.app
  return app


def looger_handler():
    log_format = '[Flask-log] File:\"%(filename)s\" [%(asctime)s] line:%(lineno)s %(levelname)s:%(message)s'
    logging.basicConfig(level='DEBUG', format=log_format, stream=sys.stderr)


gunicorn_application = create_app()

# local test
if __name__ == '__main__':
    gunicorn_application.run()
    print sys.path

