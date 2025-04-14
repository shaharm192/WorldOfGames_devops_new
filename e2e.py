from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


def test_scores_service(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        score_element = wait.until(EC.presence_of_element_located((By.ID, 'score')))
        score_text = score_element.text.strip()

        # Convert to int
        score = int(score_text)

        return 1 <= score <= 1000

    except Exception as e:
        print(f"Error during test: {e}")
        return False

    finally:
        driver.quit()


def main_function():
    url = "http://localhost:8000/index.html"

    if test_scores_service(url):
        print("Test passed ✅")
        sys.exit(0)
    else:
        print("Test failed ❌")
        sys.exit(-1)


if __name__ == "__main__":
    main_function()