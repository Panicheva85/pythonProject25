#python -m pytest -v --driver Chrome --driver-path chromedriver test_selenium_petfriends.py

import time

def test_petfriends(selenium):
   # Open PetFriends base page:
   selenium.get("https://petfriends.skillfactory.ru/")

   time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

   # click on the new user button
   btn_newuser = selenium.find_element_by_css_selector("div:nth-child(6) > button")
   btn_newuser.click()

   # click existing user button
   btn_exist_acc = selenium.find_element_by_css_selector("div.text-center > a")
   btn_exist_acc.click()

   # add email
   field_email = selenium.find_element_by_css_selector("input#email")
   field_email.clear()
   field_email.send_keys("nata123456@mail.ru")

   # add password
   field_pass = selenium.find_element_by_css_selector("input#pass")
   field_pass.clear()
   field_pass.send_keys("123456")

   # click submit button
   btn_submit = selenium.find_element_by_css_selector("div.text-center > button")
   btn_submit.click()

   time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

   assert  selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"
