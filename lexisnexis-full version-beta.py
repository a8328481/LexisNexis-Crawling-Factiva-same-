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
            self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
            search_frame = self.driver.find_element_by_xpath("//input[@id = 'terms']")
            search_frame.send_keys(self.key)
            self.driver.find_element_by_xpath("//div[@id='advHeader']//img").click()
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "State and Federal Cases"))).click()
            self.driver.find_element_by_id("Law Reviews").click()
            self.driver.find_element_by_id("Company Profiles").click()
            self.driver.find_element_by_id("txtFrmDate").send_keys(self.start_date)
            self.driver.find_element_by_id("txtToDate").send_keys(self.end_date)
            self.driver.find_element_by_xpath("//input[@id='OkButt']").click()
            search_button = self.driver.find_element_by_xpath("//input[@id='srchButt']")
            search_button.click()
        except:
            pass

    def predownload_action(self):
        try:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "mainFrame"))))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//frame[@title='Results Content Frame']"))
            Select(self.driver.find_element_by_xpath("//select[@class='goog-te-combo']")).select_by_value('en')
            a_tag = self.driver.find_element_by_xpath("//tbody/tr[@class='noshaderow1st']/td/a")
            first_url = a_tag.get_attribute('href')
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.driver.find_element_by_id("mainFrame"))
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//frame[@title='Results Navigation Frame']"))
            self.Count_of_article = self.driver.find_elements_by_tag_name("strong")[1].text
            print self.Count_of_article
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
            download_page = self.driver.window_handles[1]
            original_page = self.driver.window_handles[0]
            self.driver.switch_to.window(download_page)
            select_button = self.driver.find_element_by_id('sel')
            select_button.click()
            if int(self.Count_of_article)>int(500):
                select_doc = self.driver.find_element_by_id('rangetextbox')
                select_doc.send_keys('1-500')
                format= Select(self.driver.find_element_by_id('delFmt'))
                format.select_by_value('QDS_EF_GENERICTYPE')
                self.driver.find_element_by_id('briefNote').send_keys(self.key)
                download_button2 = self.driver.find_element_by_xpath("//img[@title='Download']")
                download_button2.click()
                download_link = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//p/a")))
                download_link.click()
                #back to original page

                self.driver.switch_to.window(original_page)
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame(self.driver.find_element_by_id("mainFrame"))
                self.driver.switch_to.frame(self.driver.find_element_by_xpath("//frame[@title='Results Navigation Frame']"))
                download_button = self.driver.find_element_by_xpath("//img[@title = 'Download Documents']")
                download_button.click()
                download_page = self.driver.window_handles[1]
                self.driver.switch_to.window(download_page)
                select_button = self.driver.find_element_by_id('sel')
                select_button.click()
                select_doc = self.driver.find_element_by_id('rangetextbox')
                if int(self.Count_of_article) < int(1000):
                    select_doc.send_keys('501-'+self.Count_of_article)
                else:
                    select_doc.send_keys('501-999')
                format = Select(self.driver.find_element_by_id('delFmt'))
                format.select_by_value('QDS_EF_GENERICTYPE')
                self.driver.find_element_by_id('briefNote').send_keys(self.key)
                download_button2 = self.driver.find_element_by_xpath("//img[@title='Download']")
                download_button2.click()
                download_link = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//p/a")))
                download_link.click()
                self.driver.switch_to.window(original_page)
                self.driver.get('http://www.lexisnexis.com.avoserv2.library.fordham.edu/hottopics/lnacademic/')
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
                self.driver.switch_to.window(original_page)
                self.driver.get('http://www.lexisnexis.com.avoserv2.library.fordham.edu/hottopics/lnacademic/')
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