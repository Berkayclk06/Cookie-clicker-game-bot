import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:/Development/chromedriver.exe"
cookie_url = "http://orteil.dashnet.org/experiments/cookie/"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(cookie_url)
cookie_btn = driver.find_element("css selector", "#cookie")

# 5sec control time
control_time = time.time() + 5
# 5 min stop time
stop_time = time.time() + 60 * 5

while True:
    cookie_btn.click()

    # Every 5 sec
    if time.time() > control_time:
        store_ids = driver.find_elements("css selector", "#store div b")
        # For selecting highest upgrade available
        store_ids_reverse = reversed(store_ids)

        # Convert money string to int
        money_element = driver.find_element("id", "money").text

        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Enter the store_ids list.
        for store_id in store_ids_reverse:
            # if the text is not null
            if store_id.text != '':
                # Returns the fee of the upgrade.
                selected_fee = int(store_id.text.split("-")[1].strip().replace(",", ""))
                # if cookie count is enough for upgrade do this.
                if cookie_count > selected_fee:
                    store_id.click()
                    control_time = time.time() + 5
                    break

        control_time = time.time() + 5

    # Bot will stop after 5 min and prints cookie/sec
    if time.time() > stop_time:
        print(driver.find_element("id", "cps").text)
        break

driver.quit()
