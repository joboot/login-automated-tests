from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    """
    Verify functionality of login validation

    :returns None:
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    correct_email = "email@gmail.com"
    correct_password = "password"

    incorrect_email = "incorrect" + correct_email
    incorrect_password = "incorrect" + correct_password

    correct_credentials_test(driver, correct_email, correct_password)
    incorrect_credentials_test(driver, incorrect_email, incorrect_password)
    no_credentials_test(driver)
    password_reset_success_test(driver, correct_email)
    password_reset_email_not_found_test(driver)

    driver.close()


def correct_credentials_test(driver, correct_email, correct_password):
    """
    Verify successful login with correct user credentials

    :param correct_email: Correct user email
    :param correct_password: Correct user password
    :param driver: Selenium driver for web browser
    :raises AssertionError: If test fails
    :returns None:
    """
    driver.get("https://www.hudl.com/login")
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

    email.send_keys(correct_email)
    password.send_keys(correct_password)

    login = driver.find_element(By.ID, "logIn")
    login.click()

    time.sleep(2)

    actual_url = driver.current_url
    expected_url = "https://www.hudl.com/home"

    try:
        assert actual_url == expected_url, "correct_credentials_test failed"
        print("correct_credentials_test passed")
    except AssertionError as e:
        print(e)


def incorrect_credentials_test(driver, incorrect_email, incorrect_password):
    """
    Verify unsuccessful login with incorrect user credentials

    :param incorrect_email: Incorrect user email
    :param incorrect_password: Incorrect user password
    :param driver: Selenium driver for web browser
    :raises AssertionError: If test fails
    :returns None:
    """

    driver.get("https://www.hudl.com/login")
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

    email.send_keys(incorrect_email)
    password.send_keys(incorrect_password)

    login = driver.find_element(By.ID, "logIn")
    login.click()

    time.sleep(2)

    actual_url = driver.current_url
    expected_url = "https://www.hudl.com/login"

    try:
        assert actual_url == expected_url, "incorrect_credentials_test failed"
        print("incorrect_credentials_test passed")
    except AssertionError as e:
        print(e)


def no_credentials_test(driver):
    """
    Verify unsuccessful login with no user credentials

    :param driver: Selenium driver for web browser
    :raises AssertionError: If test fails
    :returns None:
    """

    driver.get("https://www.hudl.com/login")

    login = driver.find_element(By.ID, "logIn")
    login.click()

    time.sleep(2)

    actual_url = driver.current_url
    expected_url = "https://www.hudl.com/login"

    try:
        assert actual_url == expected_url, "no_credentials_test failed"
        print("no_credentials_test passed")
    except AssertionError as e:
        print(e)


def password_reset_success_test(driver, correct_email):
    """
    Verify successful password reset with valid email address

    :param correct_email: Correct user email
    :param driver: Selenium driver for web browser
    :raises AssertionError: If test fails
    :returns None:
    """
    driver.get("https://www.hudl.com/login")
    time.sleep(2)
    need_help_link = driver.find_element(By.XPATH, '//a[@data-qa-id="need-help-link"]')
    need_help_link.click()

    time.sleep(2)

    email_input = driver.find_element(By.XPATH, '//input[@data-qa-id="password-reset-input"]')
    email_input.send_keys(correct_email)

    password_reset_button = driver.find_element(By.XPATH, '//button[@data-qa-id="password-reset-submit-btn"]')
    password_reset_button.click()

    time.sleep(2)

    actual_url = driver.current_url
    expected_url = "https://www.hudl.com/login/check-email"

    try:
        assert actual_url == expected_url, "password_reset_success_test failed"
        print("password_reset_success_test passed")
    except AssertionError as e:
        print(e)


def password_reset_email_not_found_test(driver):
    """
    Verify unsuccessful password reset with invalid email address

    :param driver: Selenium driver for web browser
    :raises AssertionError: If test fails
    :returns None:
    """
    driver.get("https://www.hudl.com/login")

    time.sleep(2)
    need_help_link = driver.find_element(By.XPATH, '//a[@data-qa-id="need-help-link"]')
    need_help_link.click()

    time.sleep(2)

    email_input = driver.find_element(By.XPATH, '//input[@data-qa-id="password-reset-input"]')
    email_input.send_keys("e")

    password_reset_button = driver.find_element(By.XPATH, '//button[@data-qa-id="password-reset-submit-btn"]')
    password_reset_button.click()

    time.sleep(2)

    actual_url = driver.current_url
    expected_url = "https://www.hudl.com/login/help#"

    try:
        assert actual_url == expected_url, "password_reset_email_not_found_test failed"
        print("password_reset_email_not_found_test passed")
    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
