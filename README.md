<h1 align="center">💬 Telegram Webhook Forwarder Bot</h1>
<p align="center">
    <em>ChatOps as a Service</em>
</p>

<p align="center">
    <img src="https://img.shields.io/github/license/TechProber/ci-bot?color=critical" alt="License"/>
    <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftechprober%2Ftelegram-webhook-forwarder-bot&count_bg=%238032AA&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/>
    <img src="https://custom-icon-badges.herokuapp.com/github/issues-pr-closed/techprober/telegram-webhook-forwarder-bot?color=purple&logo=git-pull-request&logoColor=white"/>
    <img src="https://img.shields.io/github/last-commit/techprober/telegram-webhook-forwarder-bot" alt="lastcommit"/>
</p>

## Introduction

CopyRight 2022 TechProber. All rights reserved.

Maintainer: [ Kevin Yu (@yqlbu) ](https://github.com/yqlbu)

The `telegram-webhook-forwarder-bot` forwards any incoming webhooks to the target telegram chat.

The bot is written in Python with Web Server Gateway Interface (WSGI) and Flask

## Prerequisites

Install depedencies

```bash
./install
```

Configure Environment with `.env`

```
# .env
API_TOKEN=
CHAT_ID=
WEBHOOK_PATH=
PORT=
```

Notes:

- `API_TOKEN` can be obtained by [BotFather](https://t.me/botfather?start=botostore)
- `CHAT_ID` can be obtained by sharing the chat to the [IDBot](https://t.me/username_to_id_bot?start=botostore)
- `WEBHOOK_PATH` is the api endpoint as part of the webhook url. e.g. `/webhook/hello`
- `PORT` is the port that the server listens to when running the bot locally

## Usage

Activate the virtual environment

```bash
# bash
. ./venv/bin/activate
# fish
. ./venv/bin/activate.fish
```

Spin up the local server for debugging

```bash
python3 server.py
```

## Deploy

This bot can be hosted as a serverless function. e.g hosted on [Vercel](https://vercel.com/)

```bash
# install vercel client (cli)
npm -g install vercel
# login and authenticate
verlcel
# publish a new deployment and automatically promote it to production
vercel --prod
```

## References

- [Github - pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [Vercel Advanced Python Usage - Web Server Gateway Interface](https://vercel.com/docs/runtimes#advanced-usage/advanced-python-usage/web-server-gateway-interface)
