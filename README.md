# Roblox Clothing Bot 👕👖

This project contains a set of Python scripts to automate the process of finding, downloading, and re-uploading clothing assets (shirts and pants) on the Roblox platform. The bot uses the `requests` library to interact with the Roblox website and APIs, automating tasks like logging in, searching the catalog, and uploading items to a group.

**Note:** This project, based on the code provided, appears to be from around 2017. Roblox's API has undergone significant changes since then, and the endpoints and methods used in these scripts are likely **outdated** and **will not work** as-is. For example, Roblox has deprecated the monolithic `api.roblox.com` endpoint in favor of newer, more specific microservice endpoints. Additionally, they have introduced new authentication methods, such as Open Cloud API keys, to replace cookie-based authentication for many of their services. If you're trying to run this project, it will require significant adjustments to be functional again.

-----

## 🚀 Features

  * **Automated Login**: Securely logs into a Roblox account using a username and password.
  * **Catalog Scraping**: Iterates through pages of the Roblox catalog to find clothing items.
  * **Asset Downloading**: Downloads the image templates for shirts and pants.
  * **Asset Re-uploading**: Uploads the downloaded clothing assets to a specified Roblox group.
  * **Customizable Search**: Allows you to specify the starting page number and the type of clothing to search for (shirts or pants).
  * **Rate Limiting**: Includes a configurable delay (`wait`) between requests to avoid overwhelming the server and getting rate-limited or blocked.

-----

## 📁 Files

  * `shirt.py`: The script to find, download, and re-upload **shirts**.
  * `pants.py`: The script to find, download, and re-upload **pants**.
  * `Shirts Expensive.py`: A modified version of the shirt script, specifically looking for higher-end shirts.
  * `pants Expensive.py`: A modified version of the shirt script, specifically looking for higher-end pants.

All scripts share the same core functionality, with minor variations in their configuration and features.

-----

## 🛠️ Requirements

  * Python 3
  * `requests` library
  * `Beautifulsoup` library
  * `base58` library
  * `pillow` library

You can install the required library using pip:

```bash
pip install requests
pip install Beautifulsoup
pip install base58
easy_install pillow
```

-----

## ⚙️ Configuration

Before running the scripts, you need to configure the following variables within each file:

1.  **`group_id`**: Replace `'group_id'` with the numeric ID of the Roblox group where you want to upload the clothing.
2.  **`username`**: Replace `'username'` with your Roblox account username.
3.  **`password`**: Replace `'password'` with your Roblox account password.
4.  **`starting_page`**: The catalog page number where the bot will begin its search. This is useful for continuing a task from a specific point.
5.  **`category`**: The asset category ID.
      * `'12'` for **shirts**.
      * `'14'` for **pants**.
6.  **`wait`**: The delay in seconds between each asset download and upload. A higher number is safer to prevent errors.

### Example Configuration (`shirt.py`)

```python
if __name__ == '__main__':
	# ➡️ Update these values with your information
	bot = RobloxBot(group_id = 'your_group_id')
	bot.login(username = 'your_username', password = 'your_password')
	# ➡️ Optional: adjust starting page and wait time
	bot.get_shirts(starting_page = 1, category = '12', wait = 5)
```

-----

## ▶️ Usage

To run a script, execute it from your terminal:

```bash
python shirt.py
```

The script will print its progress to the console, including login status, status errors, and successful uploads.
