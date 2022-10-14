#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple echo bot using decorators and webhook with flask
It sends the awx check-run report to the target group chat
"""

import logging
import telebot
import os
import flask

API_TOKEN = os.getenv('API_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
WEBHOOK_PORT = 8080

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)


@app.route('/webhook/awx-check-run', methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        raw_data = flask.request.get_data().decode('utf-8')
        logger.info(raw_data)
        bot.send_message(CHAT_ID, raw_data)
        return
    else:
        flask.abort(403)


# Start flask server
app.run(host='0.0.0.0', port=WEBHOOK_PORT, debug=True)
