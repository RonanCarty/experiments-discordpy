# Setup and Installation

**1. Clone the Repository:**

```
git clone https://github.com/your-username/experiments-discordpy.git
cd experiments-discordpy
```

**2. Create and Activate a Virtual Environment (optional but recommended):**

<details>

<summary>Windows</summary>

```
python3 -m venv venv
venv\Scripts\activate
```

</details>

<details>

<summary>MacOS/Linux</summary>

```
python3 -m venv venv
source venv/bin/activate
```

</details>

**3. Install Dependencies (Ensure you have ACTIVATED the Virtual Environment if you set one up):**

```
pip install -r requirements.txt
```

**4. In the bot directory, rename the `.env.example` file to `.env` and add your Discord bot token and other necessary environment variables.**

**5. Run the bot (Ensure you have ACTIVATED the Virtual Environment if you set one up):**

```
python bot/main.py
```
