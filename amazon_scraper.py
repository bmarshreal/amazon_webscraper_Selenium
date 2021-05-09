from selenium import webdriver

def launchBrowser():
    print('Please enter an item to look for on Amazon')
    searchFor = input()
    
    PATH = 'C:\Program Files (x86)\chromedriver.exe' #Must manually type (NO COPY PASTE!!)
    driver = webdriver.Chrome(PATH)
    
    driver.get('https://amazon.com')

#elem = driver.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a')
#elem.click()
#elem = driver.find_elements_by_css_selector('p')
#print(len(elem))
    searchElem = driver.find_element_by_css_selector('#twotabsearchtextbox')

    searchElem.send_keys(searchFor)
    searchElem.submit()
    while(True):
        pass

launchBrowser()