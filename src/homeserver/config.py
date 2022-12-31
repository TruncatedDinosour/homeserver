#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""homeserver config"""

from secrets import SystemRandom
import os

_prod: bool = os.environ.get("PROD") is not None

HOST: str = "0.0.0.0" if _prod else "127.0.0.1"
PORT: int = 80 if _prod else 8080

RANDOM: SystemRandom = SystemRandom()

# this get populated automatically, but you can add more if it cant detect your app as valid
SUBAPPS: dict[str, str] = {}

DB_DIR: str = "db"