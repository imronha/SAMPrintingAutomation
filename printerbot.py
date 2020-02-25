from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login_info import username, password
import time
import pyautogui


class PrinterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        # Navigate to 8SAM Login page
        self.driver.get(
            'https://samadmin.azurewebsites.net/login.aspx')

        # Select the username field and type in username
        username_in = self.driver.find_element_by_xpath(
            '//*[@id="txtLoginID"]')
        username_in.send_keys(username)

        # Select the password field and type in password
        password_in = self.driver.find_element_by_xpath(
            '//*[@id="txtPassword"]')
        password_in.send_keys(password)

        # Click login button
        login_btn = self.driver.find_element_by_xpath('//*[@id="btnLogin"]')
        login_btn.click()

    def nav_to_print(self):
        # Click on "Worksheets" button
        worksheet_btn = self.driver.find_element_by_xpath(
            '//*[@id="lnk1"]/p/img')
        worksheet_btn.click()

        # Click on "Print Worksheets" button
        print_worksheet_btn = self.driver.find_element_by_xpath(
            '//*[@id="AIcolumns_NaviContainer"]/div/ul/li[2]/a[2]')
        print_worksheet_btn.click()

    def keyboard_shortcut_print(self):
        # Hold 'command' and 'option' key
        pyautogui.keyDown('command')
        pyautogui.keyDown('option')
        # Press and release 'P' key
        pyautogui.press('p')
        # Release 'command' and 'option' key
        pyautogui.keyUp('command')
        pyautogui.keyUp('option')

    def print_all(self):
        # Start function once base window is closed
        base_window = self.driver.window_handles[0]
        while True:
            if self.driver.window_handles[0] != base_window:
                windows_length = len(self.driver.window_handles)
                # Iterate through pdf windows and runs print command for x number of windows
                for x in range(windows_length):
                    # print(self.driver.window_handles)
                    self.driver.switch_to_window(self.driver.window_handles[0])
                    time.sleep(3)
                    # Open print dialogue
                    # Hold 'command' and 'option' key
                    pyautogui.keyDown('command')
                    pyautogui.keyDown('option')
                    pyautogui.press('p')
                    pyautogui.keyUp('command')
                    pyautogui.keyUp('option')
                    time.sleep(3)
                    pyautogui.press('enter')
                    # pyautogui.click(print_btn_location)
                    # Wait for print job to send?
                    print('Successfully printed a PDF from window ' +
                          self.driver.window_handles[0])
                    time.sleep(3)
                    print('Wait 3 seconds completed')
                    # Close current pdf after printing
                    self.driver.close()
                    # .close() removes the window from the window_handles array
                print('Successfully printed all PDFs!')
                break


new_bot = PrinterBot()
new_bot.login()
new_bot.nav_to_print()
new_bot.print_all()
