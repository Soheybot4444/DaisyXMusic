# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "BAB6ynfiva2JMNojF5TFU73qqTgQnxZ1RXlk3A8zcC_MitmkOQExcjOO3Ic0oy4F1MZ0BhnBr3RM-s-tozhsIw47S_97cKGBOCWS0OrUMOJ90wFMkL1rYmlI9DrvK9EYjSsJAffV8jJKOwwIMOlJ5iGxkIvi7mSGN4MiDaAVdAydvVH9tMgY0TD8WMRRtoLWR9MIYhhvuJkM_0qpLZkja1harhJIh4z2orBU4mZSIHQN6j0jYoiV_PeMx5QZEKkgz8iYAeo1TPhy42x6ZLciNfMn9X_oJLPZVIY0hUYxwY0xvdbijtLDs_0Lgc6F5FdqRRCXKfnhnwer2Hlu-zbzYybgYzw9UQA"
BOT_TOKEN = "1785461638:AAFM9uQeeBkh-yD6lGpYxLGKNHwDrf2HYTQ"
BOT_NAME = "Music Player"
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@DaisyXupdates")
BG_IMAGE = "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png"
admins = {}
API_ID = 4328913
API_HASH = "3230ec801f78a517c9a2ad6bebb7f7b4"
DURATION_LIMIT = 7
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
