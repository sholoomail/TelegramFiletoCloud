## What is about this bot ?

#### This bot uploads telegram files to a third-party server.
#### Usage: Send any file or bot. Then select the third-party server you want to upload to.


### Installation
#### Clone

```sh
git clone https://github.com/AbhijithNT/TelegramFiletoCloud.git

cd TelegramFiletoCloud

```

#### Install Requirements

```sh
pip3 install -U -r requirements.txt
```
#### Edit Sample_config.py and replace it with your bot details like this

```python3
class Config:
    BOT_USE = False                        # True is private use
    BOT_TOKEN = ''                         # from @botfather
    APP_ID =                               # from https://my.telegram.org/apps
    API_HASH = ''                          # from https://my.telegram.org/apps
    AUTH_USERS = []                        # Private users id
```

#### Run this bot
```sh
python3 -m bot
```

### Heroku Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sholoomail/TelegramFiletoCloud/)

## :clap:  Supporters
[![Stargazers repo roster for @Abhijith-cloud/TelegramFiletoCloud](https://reporoster.com/stars/AbhijithNT/TelegramFiletoCloud)](https://github.com/Abhijith-cloud/TelegramFiletoCloud/stargazers)
[![Forkers repo roster for @Abhijith-cloud/TelegramFiletoCloud](https://reporoster.com/forks/AbhijithNT/TelegramFiletoCloud)](https://github.com/Abhijith-cloud/TelegramFiletoCloud/network/members)
