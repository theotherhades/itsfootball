import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

op = webdriver.ChromeOptions()
op.add_argument("headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options = op)

driver.get("https://football-vs-soccer--hyperhacker.repl.co/")
time.sleep(2)

idx = 1
while True:
    driver.execute_script("socket.emit(\"click\", \"football\")")
    print(idx)
    idx += 1