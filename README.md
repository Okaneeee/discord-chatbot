# 🤖 Discord Chatbot

A simple chatbot for Discord using Python and the [Discord.py](https://discordpy.readthedocs.io/en/stable/) library. </br>
The chatbot is using the [NeuralIntents](https://github.com/NeuralNine/neuralintents/) library for neural networks and training. It is a small-scale neural network with a small dataset.*</br>
The chatbot is also using the [Urban Dictionary API](https://unofficialurbandictionaryapi.com) to search for some information on the internet.\*

**It's not always accurate, it's made for personal and educational purposes. Use it at your own risk.*

## Table of Content
<details>
  <summary> Click me! </summary>

  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Quick Start](#quick-start)
  - [Project Status](#project-status)
  - [Features](#features)
  - [Examples](#examples)
    - [⚜️ Slash commands](#-slash-commands)
    - [🤖 Chatbot](#-chatbot)
    - [🔎 Searching](#-searching)
  - [Inspiration and sources](#inspiration-and-sources)
  - [Copyrights](#copyrights)

</details>

## Getting Started

### Installation

<details>
  <summary> Instructions for cloning with git </summary>

  - Open a terminal and navigate to the directory where you want to clone the repo.
  - Run the following commands:
  ```bash
  git clone https://github.com/Okaneeee/discord-chatbot.git
  cd discord-chatbot
  ```

</details>

</br>

<details>
  <summary> Instructions for downloading the zip </summary>

  - Click on the green `Code` button and select `Download ZIP`. Or click [here](https://github.com/Okaneeee/discord-chatbot/archive/refs/heads/main.zip)
  - Extract the zip file to the directory where you want to clone the repo.
  - Open a terminal in the folder where you extracted the zip file and run the following command:
  ```bash
  cd discord-chatbot
  ```

</details>

</br>

This repo was made with Python ``3.11.7``. You can check the working versions of Python for this repo [here](#project-status). </br>

The repo uses some dependencies. You can install them by running the following command:
```bash
pip install -r requirements.txt
```

### Quick Start
You'll need to setup a `.env` file first. The `.env` need to be on the same folder as the repo. You can use the following template, or you can rename the [`.env.example`](./.env.example) file to `.env`.

```env
TOKEN =
GUILD = 
OWNID = 
```

**TOKEN** is the bot token you get from the [Discord Developer Portal](https://discord.com/developers/applications). </br>
*More information [here](https://discord.com/developers/docs/getting-started#configuring-your-bot).* </br>

**GUILD** is the server ID you want the bot be active on. You can remove this field but you'll need to remove it on the [`main.py`](./src/main.py) file too. </br>
*More information on how to get your server ID [here](https://support.discord.com/hc/en-us/articles/206346498).*

**OWNID** is the bot's ID. It is used as a prefix for the bot (when you're mentioning (@) it). You can remove this field but you'll also need to remove it on the [`main.py`](./src/main.py) file and set a new prefix. </br>
*More information on how to get the bot ID [here](https://support.discord.com/hc/en-us/articles/206346498).*
</br></br>

After, you'll need to [add your bot to your server](https://discord.com/developers/docs/getting-started#installing-your-app). </br>
Finally, you can run the bot by running the following command:

```bash
python src/main.py
```

## Project Status

<details>
  <summary> The repo's dependencies are tested with the following versions of Python: </summary>

| Version             | Done | Status |
|-------------------------|------|--------|
| Python 3.7 | ❌ | Too old |
| Python 3.8 | ✔ | [![Python 3.8](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python38.yml/badge.svg)](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python38.yml) |
| Python 3.9 | ✔ | [![Python 3.9](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python39.yml/badge.svg)](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python39.yml) |
| Python 3.10 | ✔ | [![Python 3.8](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python310.yml/badge.svg)](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python310.yml) |
| Python 3.11 | ✔ | [![Python 3.8](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python311.yml/badge.svg)](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python311.yml) |
| Python 3.12 | ✔ | [![Python 3.8](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python312.yml/badge.svg)](https://github.com/Okaneeee/discord-chatbot/actions/workflows/python312.yml) |

</details>

Checking code quality with these actions:

| Actions             | Done | Status |
|-------------------------|------|--------|
| Spelling | ✔ | [![Spelling](https://github.com/Okaneeee/discord-chatbot/actions/workflows/spelling.yml/badge.svg)](https://github.com/Okaneeee/discord-chatbot/actions/workflows/spelling.yml) |
| CodeQL | ✔ | [![CodeQL](https://github.com/Okaneeee/discord-chatbot/actions/workflows/codeql.yml/badge.svg)](https://github.com/Okaneeee/discord-chatbot/actions/workflows/codeql.yml) |

## Features

- [x] Slash commands
- [x] A small-scale chatbot that can answer some question*
- [x] Can search for some information on the internet using the [Urban Dictionary API](https://unofficialurbandictionaryapi.com)*
</br></br>

**The chatbot is still in development and it's not perfect. It's using a small dataset and it's not trained to answer all questions. It's also not able to understand the context of the conversation. It's a simple chatbot that can answer some questions and search for some information on the internet. The search part is not optimized and is not working everytime.*

## Examples:

### ⚜️ Slash commands

<details>
<summary> Example </summary>

![Slash commands](./img/ie_slash.png)

</details>

### 🤖 Chatbot

<details>
<summary> Example </summary>

![Chatbot](./img/ie_chatting.png)

</details>

### 🔎 Searching

<details>
<summary> Examples </summary>

![Searching 1](./img/ie_search1.png)
![Searching 2](./img/ie_search2.png)

</details>

## Inspiration and sources
This project was inspired by the [NeuralNine's video](https://youtu.be/urlkrueSXpI) on how to create a chatbot using Python and Deep Learning. </br>
You can also look at tatiblockchain's [python deep learning chatbot](https://github.com/tatiblockchain/python-deep-learning-chatbot) for a similar project using Flask. </br>
Some part are written with the help of [GitHub Copilot](https://copilot.github.com/).

## Copyrights
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.</br>
This include all contributions to the project, even from the community.

Copyright © 2024 Okane
