# Amazon Webscraping (Educational)

Scrapes product details from an Amazon product page using Selenium (Safari) + BeautifulSoup, then saves the results to a CSV.

## What it does
- Opens the product page in Safari via Selenium
- Extracts title, price, rating, bullets, tech details, and review snippets
- Writes data to `amazon_airpod_max.csv`

## Requirements
- Python 3.10+
- macOS Safari
- Safari WebDriver enabled (Develop → Allow Remote Automation)
- Python packages: `selenium`, `beautifulsoup4`, `lxml`

## Setup
Activate the virtual environment (already in this repo):

```zsh
source /Users/rawanalsaleh/python_webscraping/ws_env/bin/activate
```

If you need to install dependencies:

```zsh
pip install selenium beautifulsoup4 lxml
```

## Enable Safari WebDriver
1. Open Safari
2. Safari → Settings → Advanced → enable “Show features for web developers”
3. Develop → “Allow Remote Automation”

## Run
```zsh
python app.py
```

## Output
- CSV file: `amazon_airpod_max.csv`
- Console logs for the scraped fields

## Notes
- Amazon may present CAPTCHAs or block automated access. If that happens, wait and retry.
- This is for learning purposes; follow Amazon’s Terms of Service.

## Optional: Chrome headless (alternate)
If you switch to Chrome, you can run headless mode by using Selenium’s Chrome options (not currently configured in `app.py`).