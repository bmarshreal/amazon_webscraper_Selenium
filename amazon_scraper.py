from selenium import webdriver

def launchBrowser():
    print('Please enter an item to look for on Amazon')
    searchFor = input()
    
    PATH = 'C:\Program Files (x86)\chromedriver.exe' #Must manually type (NO COPY PASTE!!)
    #Local absolute path to chromedriver.exe
    driver = webdriver.Chrome(PATH)
    #Connecting Seleniums webdriver to chromedriver
    driver.get('https://amazon.com')
    #GET response from the given URL

#elem = driver.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a')
#elem.click()
#elem = driver.find_elements_by_css_selector('p')
#print(len(elem))

    searchElem = driver.find_element_by_css_selector('#twotabsearchtextbox')
    #Find an CSS Selector of interest to manipulate (In this case a searchbox)
    
    searchElem.send_keys(searchFor)
    #Define keys for Selenium to enter into the searchbox we selected above
    searchElem.submit()
    #Submit our search
    while(True):
        pass
        #Keep Selenium from closing itself
launchBrowser()