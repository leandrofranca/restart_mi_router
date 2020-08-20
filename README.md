# Restart Mi Router 3

A script to automatically restart Mi Router 3 using Selenium.

## Installation
1. Install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (or an alternatie driver for your browser of choice).
2. Download this source code in a virtual-env:
   * `$ git clone git@github.com:leandrofranca/restart_mi_router.git`
   * `$ python -m venv restart_mi_router`
3. Run virtual environment:
   * `$ cd restart_mi_router`
   * `$ source bin/activate`
4. Install Requirements: `$ pip install -r requirements.txt`

## Usage
#### To run the entire script:
1. Run `$ python apply.py [mi_router_password]`
2. From there on, everything is automatic!


## Thanks
* [Selenium](https://selenium-python.readthedocs.io/) - A tool designed for QA testing, but that actually works great for making these types of bots
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/doc) - A tool to scrape HTML/XML content (that saved be *big time* with this project)
