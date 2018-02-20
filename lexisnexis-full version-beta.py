from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import Select
import pandas as pd


class LexisNexis():
    def __init__(self, username=******, password=******, key="IBM"):
        self.username = username
        self.username = username
        self.password = password
        self.key = key
        self.driver = webdriver.Chrome('C:\Users\lhuang54\Desktop\chromedriver')
        self.driver.get('http://www.lexisnexis.com.avoserv2.library.fordham.edu/hottopics/lnacademic/')

        #self.log_in()
        for startdate, enddate in zip(['5/1/2015','5/1/2013','5/1/2011','5/1/2009','5/1/2007'],['5/1/2017','5/1/2015','5/1/2013','5/1/2011','5/1/2009']):
            self.start_date = startdate
            self.end_date = enddate
            self.search()
            sleep(3)
            self.predownload_action()
            self.download_doc()
        self.driver.quit()
        #self.open_target_profile()
        #self.scroll_down_target_profile()
    def log_in(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.NAME, "user"))).send_keys(self.username)
        password_frame = self.driver.find_element_by_xpath("//input[@name='pass']")
        password_frame.send_keys(self.password)
        submit_frame = self.driver.find_element_by_xpath("//input[@name='submit']")
        submit_frame.click()

    def search(self):
        try:
            *********
            DEALING WITH FRAME QUESTION , EMAIL: lhuang54@fordham.edu
            *********
        except:
            pass

    def predownload_action(self):
        try:
            *********
            DEALING WITH FRAME QUESTION , EMAIL: lhuang54@fordham.edu
            *********
        except:
            pass

        #self.basic_url = first_url[:-1]
    def download_doc(self):
        try:
            download_button = self.driver.find_element_by_xpath("//img[@title = 'Download Documents']")
            download_button.click()
            sleep(3)
            a = self.driver.page_source
            print a
            
            
            
            *********
            DEALING WITH pop-up WINDOW QUESTION , EMAIL: lhuang54@fordham.edu
            *********
            
            
            
            else:
                select_doc = self.driver.find_element_by_id('rangetextbox')
                select_doc.send_keys('1-'+self.Count_of_article)
                format = Select(self.driver.find_element_by_id('delFmt'))
                format.select_by_value('QDS_EF_GENERICTYPE')
                self.driver.find_element_by_id('briefNote').send_keys(self.key)
                download_button2 = self.driver.find_element_by_xpath("//img[@title='Download']")
                download_button2.click()
                download_link = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//p/a")))
                download_link.click()
                
                
                *********
                DEALING WITH pop-up WINDOW QUESTION , EMAIL: lhuang54@fordham.edu
                *********
        except:
            pass

if __name__ == "__main__":
    company_list=pd.read_excel(r'C:\Users\lhuang54\unCrawl.xlsx',sheetname = 'Sheet1')
    for NAME in company_list['finished']:
        a = LexisNexis(key = NAME)

"""
        self.driver.find_element_by_xpath("//img[@class='ui-datepicker-trigger']").click()
        Select(self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']")).select_by_value('2016')
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendaer']/tbody/tr/td/a[text()='1']").click()
        self.driver.find_element_by_xpath("//img[@class='ui-datepicker-trigger']").click()
        Select(self.driver.find_element_by_xpath("//select[@class='ui-datepicker-year']")).select_by_value('2016')
        self.driver.find_element_by_xpath("//table[@class='ui-datepicker-calendaer']/tbody/tr/td/a[text()='1']").click()

"""
