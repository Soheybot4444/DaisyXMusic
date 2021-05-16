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
SESSION_NAME = "BACatrAizbsP1eKBmNvfdTUZQKd7YeUGG9tSXPeQwqZmtMPfSa67teanSCN8hFjbLbUYI6nCQODOgpwozf28EoX1V73G6iliKQkvHBC_477HXRicn2qMhmBhvCqft6c5xy29VITpwgbMeD-2YdhOxl28uBs3A2oiJoe1xWUhjZz1XFPEDnuWLjE310rDXAMvriJ1Ip8Fkr5GRzpD725gyXKEPZYk_2AATOPxkiLZXDDhBy8dA0ITYujwZbR38BCq_OY6kv_ham3D1oYCS3gdMxQ1a0yEGXPzUfEp5mGYXbHUYZbo3RAmr2_S2uteIRyMVsxm_02a3_YaJ7MOnf02z8mrYzw9UQA"
BOT_TOKEN = "1785461638:AAFM9uQeeBkh-yD6lGpYxLGKNHwDrf2HYTQ"
BOT_NAME = "Music Player"
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@DaisyXupdates")
BG_IMAGE = "https://telegra.ph/file/f27e5ffdc2ca4406952b8.jpg"
admins = {}
API_ID = 4328913
API_HASH = "3230ec801f78a517c9a2ad6bebb7f7b4"
DURATION_LIMIT = 15
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = "1601268629"
