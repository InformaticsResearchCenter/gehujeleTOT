from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyunpack import Archive
import shutil, os

class Chatbot(object):
    def saveProfile(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--user-data-dir=./user_data")
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def openBrowser(self):
        self.saveProfile()
        self.driver.get("https://web.whatsapp.com/")
        self.waitLogin()

    def waitLogin(self):
        self.target = '"_3ZW2E"'
        self.x_arg = "//div[contains(@class, " + self.target + ")]"
        self.wait = WebDriverWait(self.driver, 600)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.x_arg)))

    def typeAndSendMessage(self, message):
        self.message_target = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        self.message_target.send_keys(message)
        self.sendbutton = self.driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        self.sendbutton.click()

    def moveFiles(self, namafile):
        move = True
        while move:
            try:
                source = 'C:\\Users\\trian\\Downloads\\' + str(namafile)
                destination = r'C:\Users\trian\gehujeleTOT'
                shutil.move(source, destination)
                move = False
            except Exception as e:
                if 'already exists' in str(e):
                    move = False
                else:
                    move = True

    def makeDirectory(self):
        mkdir = True
        create = '1'
        while mkdir:
            try:
                os.mkdir(str(create))
                mkdir = False
            except:
                create = int(create) + 1
                mkdir = True
        return create

    def extractFiles(self, namafile):
        try:
            create=self.makeDirectory()
            Archive(namafile).extractall('.\\' + str(create))
            result = []
            path=r'.\{folder}'.format(folder=create)
            for root, dirs, files in os.walk(path):
                for i in files:
                    if '.pdf' in i:
                        result.append(os.path.join(root, i))
            for i in result:
                self.typeAndSendMessage(str(i))
            os.remove(namafile)
            shutil.rmtree(path)
        except:
            result=''
            self.typeAndSendMessage('file must be .zip or .rar')
            os.remove(namafile)
            os.rmdir(create)
        return result

    def cekAndSendMessage(self):
        while True:
            try:
                try:
                    self.chat = self.driver.find_elements_by_class_name("OUeyt")[0]
                    self.chat.click()
                    self.chat.click()
                    self.chat.click()
                except:
                    print("no notification")
                self.message = self.driver.find_elements_by_xpath("(.//span)")[-11].text
                self.message = self.message.lower()
                if "wanda download file" in self.message:
                    try:
                        filecheck=self.driver.find_elements_by_class_name('_2RBFb')[-1]
                        namafile=self.driver.find_elements_by_class_name('_3UPcK')[-1].text
                        self.driver.find_elements_by_class_name('_17viz')[-1].click()
                        self.typeAndSendMessage('sudah di download yaaa...')
                        self.moveFiles(namafile)
                        self.extractFiles(namafile)
                    except:
                        self.typeAndSendMessage('ga ada filenya....')
            except Exception as e:
                print(e)
                print("No Message..")