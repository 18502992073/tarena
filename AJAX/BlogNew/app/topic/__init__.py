"""
声明蓝图程序，负责代替app声明路由
"""
from flask import Blueprint

topic_app = Blueprint("topic", __name__)
from . import viwes
