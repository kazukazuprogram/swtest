#!/usr/bin/env python3
#coding: utf-8

from bottle import route, run, get
from os.path import join

@get("/")
def root():
    with open(join(".", "index.html"), encoding="utf8") as fp:
        return fp.read()

@get("/<filename>")
def rootfile(filename):
    if filename == "favicon.ico":
        return
    with open(join(".", filename), encoding="utf8") as fp:
        return fp.read()

if __name__ == "__main__":
    run(host="0.0.0.0", port=80)
