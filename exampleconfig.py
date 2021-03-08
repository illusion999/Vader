from sample_config import Config


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 2700515
  API_HASH = "1f8f17628750e828cb0ee0cae17957cb"

  # the name to display in your alive message.
  # If not filled anything then default value is Hell User.
  ALIVE_NAME = "XERX"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://vyxzdunx:l2877V7lvvpZERgV6kkOemOnO-HW4BG1@ziggy.db.elephantsql.com:5432/vyxzdunx"

  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  STRING_SESSION = "1AZWarzoBu8MHnVrhQv9_ixrUY4l4bsbxabPvVahVgp_I94x4KJ8W4U8ypswa5bcG3vCOvxGZbB6Nn6iQ-YcKSyT97MiYR2QGYhHjNuyEpO7e1XGvENpVtFXRmKMyujFcSz70THRAMAbUOVALkMQ549k8yD3V9aMqMRSBrjWXsD-R4W_7D_uATCtd1r2qRReW64xsmE8ntDq9HK35IMQKhNvpv2PDFNJ4w3oJ_-9PDtDAa7XffBJSy5-5nh5rm4SD1VbbeY8z-Onlw2W8bYHWqSN3OHSfVhMSKu-_DYFJFoHJ8qcg3GVE4YdYdRDatwr2BGyBQr-lolsJl4W-1-QnaYe6jSnF1Qo="

  # Create a bot in @botfather and fill the following values with bot token and username.
  BOT_TOKEN = "1633658116:AAEakff-NOxkzNH3w81Uy2NTALz5CJzkmPM" #token
  BOT_USERNAME = "@Xerxx35bot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  LOGGER = -1001309372845

  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = [1410616929]
