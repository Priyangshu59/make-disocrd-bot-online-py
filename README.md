# Discord Online Bot

A simple Discord bot made with Python using `discord.py`.

This bot only comes online and stays connected to Discord.

---

# Setup Guide

## 1. Clone The Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

---

## 2. Open The Project Folder

```bash
cd YOUR_REPOSITORY
```

---

## 3. Install Required Package

```bash
pip install discord.py
```

---

# Create Your Discord Bot

## 1. Open Discord Developer Portal

https://discord.com/developers/applications

---

## 2. Create A New Application

- Click `New Application`
- Enter a bot name
- Click `Create`

---

## 3. Add A Bot

- Open the `Bot` section
- Click `Add Bot`

---

## 4. Copy Your Bot Token

Inside the Bot section:

- Click `Copy Token`

---

# Configure The Bot

Open:

```bash
bot.py
```

Replace:

```python
"YOUR_BOT_TOKEN"
```

with your actual Discord bot token.

Example:

```python
bot.run("YOUR_REAL_TOKEN")
```

---

# Run The Bot

```bash
python bot.py
```

If everything is correct, the bot will come online in Discord.

---

# Invite The Bot To Your Server

Open:

```bash
OAuth2 → URL Generator
```

Select:

- `bot`

Choose the permissions you want and open the generated invite URL in your browser.

---

# License

MIT License
