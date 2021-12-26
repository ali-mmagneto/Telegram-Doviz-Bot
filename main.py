#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

    app = pyrogram.Client(
        "X-URL-Uploader",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=datalar
    )
    app.run()
