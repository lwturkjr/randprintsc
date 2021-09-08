import random
import string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions() 
options.add_argument("window-size=1600,900")
options.add_argument('--disable-blink-features=AutomationControlled')
browser  = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
#print(browser.execute_script("return navigator.userAgent;"))

letters = string.ascii_lowercase
numbers = string.digits

lets = ''.join(random.choice(letters) for i in range(2))
nums = ''.join(random.choice(numbers) for i in range(4))

img = lets + nums

# Open the Website
browser.get("https://prnt.sc/"+img)

