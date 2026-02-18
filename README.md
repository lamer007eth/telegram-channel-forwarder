# Telegram Channel Forwarder 📡➡️📬

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Telegram](https://img.shields.io/badge/Telegram-Telethon-2CA5E0)
![Type](https://img.shields.io/badge/Type-Message%20Relay-purple)
![Monitoring](https://img.shields.io/badge/Monitoring-Multi--Channel-orange)
![Infra](https://img.shields.io/badge/Infra-Signal%20Router-grey)

Multi-channel Telegram forwarder that monitors multiple source channels, applies filtering rules and relays messages to a target channel in real time.

---

## ✨ Features

* 📡 Monitors multiple Telegram channels simultaneously
* 📬 Instantly forwards new messages
* 🧠 Supports filtered forwarding logic
* 🏷️ Channel-specific filters
* 🔁 Auto-reconnect on connection loss
* 🔐 Uses Telegram user API (Telethon)
* ⚡ Real-time signal relay

---

## 📦 Project structure

```text
telegram-channel-forwarder/
├─ telegram_channel_forwarder.py
├─ .env.example
├─ requirements.txt
├─ .gitignore
└─ README.md
```

---

## 🚀 Quick start

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2) Get Telegram API credentials

Go to:

https://my.telegram.org

Create an app → get:

* API_ID
* API_HASH

---

### 3) Configure `.env`

Copy:

```
.env.example → .env
```

Fill:

```env
API_ID=1234567
API_HASH=your_api_hash

TARGET_CHANNEL=username

FULL_FORWARD_CHANNELS=Channel_1,Channel_2,Channel_3
FILTERED_CHANNEL=Channel_name

RECONNECT_DELAY=5
SESSION_NAME=forwarder_session
```

---

### 4) Run

```bash
python telegram_channel_forwarder.py
```

First run will ask for Telegram login code.

---

## 🧠 Filtering logic

Example implemented:

Messages from `FILTERED_CHANNEL` are forwarded **only if** they contain:

```
Collection Link: https://t.me/sticker_bot/
```

All other monitored channels are forwarded fully.

Filtering rules can be customized in code.

---

## 🔄 How it works

1. Connects via Telegram user API
2. Listens to new messages in source channels
3. Applies optional filters
4. Forwards messages to target channel
5. Auto-reconnects if connection drops

---

## 📡 Use cases

* Alpha / signal aggregation
* NFT mint alerts
* Trading signals relay
* Private research feeds
* Monitoring announcement channels

---

## 🔐 Security notes

* `.session` file stores Telegram login session
* Do NOT commit session files
* `.env` contains API credentials
* Use `.gitignore` to protect secrets

---

## 🛠️ Requirements

```txt
telethon
python-dotenv
```

---

## ⚠️ Disclaimer

For educational and monitoring purposes only.
Use responsibly and respect Telegram Terms of Service.
