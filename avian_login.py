from selenium import webdriver
import time

url = 'https://avian.lib.iastate.edu'
driver = webdriver.Firefox()

# To handle Okta logins, we need to wait for the login
# page's scripts to populate the HTML form elements
driver.implicitly_wait(10)

def login(driver, username, password):
    login_btn_xpath = '//a[@href="/_webdev/auth/login"]'
    
    driver.get(url)
    driver.find_element_by_xpath(login_btn_xpath).click()

    username_field = driver.find_element_by_id('okta-signin-username')
    password_field = driver.find_element_by_id('okta-signin-password')

    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element_by_id('okta-signin-submit').click()

    # If we don't pause here, the login fails. By pausing we keep
    # from short-circuiting Okta & Shibboleth.
    time.sleep(2)
    
    driver.get(url)
