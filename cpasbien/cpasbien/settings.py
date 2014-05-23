# Scrapy settings for cpasbien project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cpasbien'

SPIDER_MODULES = ['cpasbien.spiders']
NEWSPIDER_MODULE = 'cpasbien.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'cpasbien (+http://www.cpasbien.pe)'

# Log Settings
LOG_ENABLED = True
LOG_LEVEL = 'INFO' # Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
LOG_FILE = './cpasbien.log'
