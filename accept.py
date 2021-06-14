from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.linkedin.com/login")
driver.maximize_window()


driver.find_element_by_id("username").send_keys("<username>") #Enter your username here
driver.find_element_by_id("password").send_keys("<password>") #Enter your password here
driver.find_element_by_class_name("from__button--floating").click()

driver.find_element_by_xpath("/html/body/div[5]/aside/div[1]/header/section[2]/button[2]").click() #To close the message box that pops everytime you login


driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')

buttons = driver.find_elements_by_class_name("artdeco-button--secondary" and "invitation-card__action-btn") #elements for more than 1 elements
# for button in buttons:
#     aria_label_data = button.get_attribute("aria-label")
#     if aria_label_data[0:6].lower() == "accept":
#         button.click()
for button in buttons:
    button.click()
driver.close()

