from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import config

def openBrowser():
    driver=webdriver.Chrome()
    return driver

def gotoEhaki(driver):
    driver.get('https://e-hakcipta.dgip.go.id/index.php/login')

def loginEhaki(driver):
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form[1]/div[2]/input').send_keys(config.usernamehaki)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form[1]/div[3]/input').send_keys(config.passwordhaki)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/form[1]/button').click()

def gotoResigter(driver):
    driver.get('https://e-hakcipta.dgip.go.id/index.php/register/hakcipta')

def closeBanner(driver):
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/main/div/div[2]/div/div/div[1]/button').click()

def detailForm(driver, ciptaan, judul, desk, tanggalterbit, kotaterbit):
    #jenis permohonan
    driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div/span/span[1]/span').click()
    driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
    #jenis ciptaan dan sub-jenis ciptaan
    if ciptaan.lower() == 'buku':
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div/span/span[1]/span').click()
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[3]/div/span/span[1]/span').click()
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[5]').click()
    else:
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div/span/span[1]/span').click()
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[9]').click()
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[3]/div/span/span[1]/span').click()
        driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[5]d').click()
    #judul
    driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[4]/div/input').send_keys(judul)
    #deskripsi
    driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[5]/div/textarea').send_keys(desk)
    for i in range(3):
        #time
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[6]/div/div/input[1]').click()
    for i in range(12):
        #delete time
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[6]/div/div/input[1]').send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[6]/div/div/input[1]').send_keys(tanggalterbit + Keys.ENTER)
    #kota terbit
    kota=kotaterbit.split(' ')
    newkota=[]
    for i in kota:
        newkota.append(i.capitalize())
    separator = ' '
    fixkota=separator.join(newkota)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div/main/div/div[1]/div/div/div[2]/form/div[1]/div[2]/div/div[8]/div/input').send_keys(fixkota)

if __name__ == '__main__':
    driver=openBrowser()
    gotoEhaki(driver)
    loginEhaki(driver)
    gotoResigter(driver)
    gotoResigter(driver)
    closeBanner(driver)
    detailForm(driver=driver, ciptaan='Buku', judul='ITeung', desk='ITeung merupakan bocah kecil cewe yang suka main komputer, kerjaannya setiap hari 24 jam didepan komputer', tanggalterbit='2020-01-30', kotaterbit='bandung')