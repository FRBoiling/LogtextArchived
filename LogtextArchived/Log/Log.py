#coding=utf-8
import os
import logging
import Logger

logyyx = Logger.Logger('error.log',logging.DEBUG,logging.WARN)

def debug(msg):
    logyyx.debug(msg)
def info(msg):
    logyyx.info(msg)
def war(msg):
    logyyx.war(msg)
def error(msg):
    logyyx.error(msg)
def cri(msg):
    logyyx.cri(msg)
     