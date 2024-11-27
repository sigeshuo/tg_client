FROM python:3.10.11-alpine3.18

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --no-warn-script-location --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

LABEL maintainer="SigeShuo <sigeshuo@outlook.com>" \
      version="1.0" \
      description="This is a Python Telegram session management software that supports storing Telegram login sessions as files on the user's local machine for easier automatic login in the future." \
      telegram_group="https://t.me/sigeshuo_group" \
      telegram_channel="https://t.me/sigeshuo_channel" \
      x="https://x.com/@sigeshuo"