#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple echo bot using Web Server Gateway Interface (WSGI) and Flask
The bot can be running completely as a serverless function
It receives payload data from the incoming webhooks and forward it to the target group chat
"""

import logging
import telebot
import os
import flask

from dotenv import dotenv_values
config = dotenv_values(".env")

API_TOKEN = config["API_TOKEN"]
CHAT_ID = config["CHAT_ID"]
WEBHOOK_PATH = config["WEBHOOK_PATH"]

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)


@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    if flask.request.headers.get("content-type") == "application/json":
        raw_data = flask.request.get_data().decode("utf-8")
        logger.info(raw_data)
        bot.send_message(CHAT_ID, raw_data)
        return flask.jsonify({"result": "ok!"})
    else:
        flask.abort(403)
