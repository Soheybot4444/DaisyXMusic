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
SESSION_NAME = "BABGV0ASCpLVg6LmD8B5HvJT7c5LVCRecvAi7t1JjJUD-IZoTiKu4RhgtkKb2e_O9C4iNQntLQ_tCepKXz6jpQw9-bAldZ9uxwlq-yK7oDZJoFW6KsPgR3FUi8G2Bl0o7OlJ-zLzzqzrDTubY2zVCPLzrpaYswlDeg6CKvrPTCLWR7GO2LVi_DwsOlp6LcNOqCwX5aWFLKMu6sRcL_K2dvUz4VMt_w8CbHCCWJVozsJZWxtzJ3MW-SJz2QHi5HuonT0cR8Mhm9d4Fe7C_gTf1mkfsyfXzeTQXO719t1UOTqXfM9SGrHX_jsBQKic2b_-keuy78ymwiflN2T-foGVPW51Yzw9UQA"
BOT_TOKEN = "1785461638:AAFM9uQeeBkh-yD6lGpYxLGKNHwDrf2HYTQ"
BOT_NAME = "Music Player"
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@DaisyXupdates")
BG_IMAGE = "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png"
admins = {}
API_ID = 4328913
API_HASH = "3230ec801f78a517c9a2ad6bebb7f7b4"
DURATION_LIMIT = 15
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = "1601268629"
