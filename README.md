# Experiments Discord Bot

Welcome to the **Experiments Discord Bot** project! This bot, named "Experiments," was created to test various features related to Discord bot development. It serves as a sandbox for experimenting with different functionalities, integrations, and bot behavior on the Discord platform.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## About the Project

**Experiments** is a Discord bot built using the `discord.py` library. The primary purpose of this bot is to experiment with and test various features of Discord bot development. Whether it's working with message commands, slash commands, event handling, or custom integrations, this bot is designed to help explore different possibilities in a controlled environment.

## Features

The bot is currently equipped with a range of features which you can use to help you build your own Discord bot, including but not limited to:

- Syncing the Application Commands Globally
- Checking Latency

These features are constantly evolving as new experiments and tests are conducted.

## Setup and Installation

To get the bot up and running on your own machine, follow these steps:

1. **Clone the Repository:**
  ```
  git clone https://github.com/your-username/experiments-discordpy.git
  cd experiments-discordpy
  ```

2. **Create and Activate a Virtual Environment (optional but recommended):**
  <details>
    <summary>Windows</summary>
    
    python3 -m venv venv
    venv\Scripts\activate
  </details>
  <details>
    <summary>MacOS/Linux</summary>
    
    python3 -m venv venv
    source venv/bin/activate
  </details>

3. **Install Dependencies:**
  ```
  pip install -r requirements.txt
  ```

4. **In the bot directory, rename the `.env.example` file to `.env` and add your Discord bot token and other necessary environment variables:**

5. **Run the bot (Ensure you have ACTIVATED the Virtual Environment if you did Step 2):**
  ```
  python bot/main.py
  ```

## Usage

This bot is intended for experimentation and testing. You can modify the code to add new commands, events, or integrations. Check the `main.py` file and other files in the repository to see how existing features are implemented. The main purpose of the code being open sourced is for beginner discord.py developers to understand how certain things may work. Everything in the main branch will be in full working order, other branches could be broken!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

If you have any questions or feedback, feel free to reach out:

- **GitHub: [RonanCarty](https://github.com/RonanCarty)**
- **Discord: [irishrtx](https://discordlookup.com/user/974274752669708288)**
