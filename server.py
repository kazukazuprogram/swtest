#!/usr/bin/env python3
# coding: utf-8

from gevent import monkey
monkey.patch_all()
from bottle import route, static_file, run
from os.path import join

# basepath = join(__file__, "docs")
basepath = "docs"


@route("/", method="GET")
def route_get():
    return static_file(filename="index.html", root=basepath)


@route("/<file:re:(.)+>", method="GET")
def route_get_file(file):
    return static_file(filename=file, root=basepath)


if __name__ == '__main__':
    print(basepath)
    run(port=80, debug=True, reloader=True)
