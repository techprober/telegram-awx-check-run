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
import json
import flask

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)


@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    if flask.request.headers.get("content-type") == "application/json":
        raw_data = flask.request.get_json()
        logger.info(raw_data)
        if "id" in raw_data.keys():
            payload = {
                "id": raw_data["id"],
                "name": raw_data["name"],
                "url": raw_data["url"],
                "created_by": raw_data["created_by"],
                "started": raw_data["started"],
                "finished": raw_data["finished"],
                "status": raw_data["status"],
                "inventory": raw_data["inventory"],
                "project": raw_data["project"],
                "playbook": raw_data["playbook"],
                "credential": raw_data["credential"],
                "limit": raw_data["limit"],
            }
            bot.send_message(
                CHAT_ID,
                json.dumps(
                    payload,
                    ensure_ascii=False,
                    indent=4,
                    sort_keys=True
                )
            )
        bot.send_message(
            CHAT_ID,
            json.dumps(
                raw_data,
                ensure_ascii=False,
                indent=4,
                sort_keys=True
            )
        )
        return flask.jsonify({"result": "ok!"})
    else:
        flask.abort(403)
