from aiohttp import web
from file_read_backwards import FileReadBackwards
import time
import datetime
import re


async def index(request):
    return web.Response(text='Nothing is here!')


async def last_upgrade(request):
    timpestamp = 0
    founded = False

    with FileReadBackwards("/var/log/apt/history.log", encoding="utf-8") as f:

        while True:
            line = f.readline()
            if not line:
                break

            current_config = line.split(': ')

            if current_config[0] == 'End-Date':
                timestamp = time.mktime(datetime.datetime.strptime(current_config[1].rstrip(), "%Y-%m-%d %H:%M:%S")
                                        .timetuple())
            elif current_config[0] == 'Commandline':
                cmd = current_config[1].rstrip()
                match = re.match(r'^apt(-get)? (.* )?(dist-)?upgrade( -y)?$', cmd)
                if match is not None:
                    founded = True
                    break

        if founded:
            res = {"data": {"utc-timestamp": int(timestamp)}}
        else:
            res = {"error": True, "msg": "No info about upgrade"}

    return web.json_response(res)


def setup_routes(app):
    app.router.add_routes([web.get('/', index),
                           web.get('/last-upgrade', last_upgrade)])


app = web.Application()
setup_routes(app)
web.run_app(app)
