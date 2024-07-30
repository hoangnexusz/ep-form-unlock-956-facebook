from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Back, Style, init
def create_mobile_driver():
    mobile_emulation = {
        "deviceName": "iPhone X"
    }
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)
def create_pc_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)
use_mobile = True
driver = create_mobile_driver() if use_mobile else create_pc_driver()
try:
    driver.get("https://mbasic.facebook.com")
    username_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="email"]'))
    )
    username_input.send_keys("taikhoan")
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]')
    password_input.send_keys("matkhau")
    login_button = driver.find_element(By.XPATH, '//*[@id="login_form"]/ul/li[3]/input')
    login_button.click()
    driver.implicitly_wait(10)
    current_url = driver.current_url
    new_url = current_url.replace("/intro/", "/stepper/").replace("&_rdr", "&phase=unauthenticated")
    driver.get(new_url)
    driver.implicitly_wait(10)
    continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/table/tbody/tr/td/div/div[3]/a')
    continue_button.click()
    sleep(3)
    continue_button2 = driver.find_element(By.XPATH, '//*[@id="select_challenge"]/form/div/div[3]/input')
    continue_button2.click()
    current_url = driver.current_url
    new_url2 = current_url.replace("https://mbasic.facebook.com/epsilon/select_challenge/async/?token=", "https://m.facebook.com/x/checkpoint/828281030927956/auth_wizard/intro/?token=")
    driver.get(new_url2)
    print(Fore.GREEN+f'''[URL FORM : {new_url2}]''')
    input("[Enter Để Đóng Trình Duyệt]")

finally:
    driver.quit()
