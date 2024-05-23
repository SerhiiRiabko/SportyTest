from datetime import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_live_viewers_count_present(driver):
    # Step 1: Go to Twitch
    driver.get("https://www.twitch.tv") # open site
    wait = WebDriverWait(driver, 10)

    # Step 2: Click on the search icon
    search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/nav/div[@class = "Layout-sc-1xcs6mc-0 hSqeuh"]/a')))
    search_icon.click()  # make search field an active

    # Step 3: Input "StarCraft II"
    search_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@aria-label="Search"]')))
    search_input.send_keys("StarCraft II")  # add data to search field
    search_input.send_keys(Keys.RETURN)  # results

    # Step 4: Scroll down 2 times
    for _ in range(2):
        driver.execute_script("window.scrollBy(0, window.innerHeight);")  # scroll twice
        time.sleep(2)  # Wait for the content to load

    # Step 5: Select one streamer
    streamers = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[@data-a-target="preview-card-title-link"]')))
    if streamers:
        streamers[0].click()  # if we see streamer link => click
    else:
        raise Exception("No streamers found")  # if no elements => exception is returned

    # Step 6: Validate presence of live viewers count
    time.sleep(5)  # Allow time for the streamer's page to load
    viewers_count = wait.until(EC.presence_of_element_located((By.XPATH, '//p[@data-a-target="animated-channel-viewers-count"]')))
    assert viewers_count.text.isdigit(), "Live viewers count is not present or not a numeric value."
