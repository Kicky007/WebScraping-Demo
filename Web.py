from selenium import webdriver


day = 1976


def scrapping(day):

    browser = webdriver.Firefox()

    daystr = str(day)
    site = 'CSGOEMPIRE'
    browser.minimize_window()

    browser.get('https://csgoempire.com/history?seed='+daystr)
    browser.minimize_window()
    cards = browser.find_elements_by_xpath(
        '//span[@class="block text-seed text-xxs leading-none"]')
    length = len(cards)
    f = open(site+"_"+daystr+".txt", "w")
    for i in range(length):
        f.write(cards[i].text+"\n")

    f.close()

    browser.close()


start = 1982
stop = 1985

for i in range(start, stop):
    scrapping(i)
