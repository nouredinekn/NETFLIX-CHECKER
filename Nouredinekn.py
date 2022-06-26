from selenium import webdriver
import requests
import os
import datetime

# clear console


def clear():
    os.system('cls')
# colors


class colors:
    R = '\033[91m'  # Red
    G = '\033[92m'  # Green
    Y = '\033[93m'  # Yellow
    B = '\033[94m'  # Blue
    P = '\033[95m'  # Purple
    C = '\033[96m'  # Cyan
    W = "\033[1;37m"  # White
    bold = '\033[1m'
    unbold = '\033[0m'

# telegram config


class getTgInfo:
    try:
        tlg = open('telegram.txt', 'r').read()
        token = tlg.split('|')[0]
        id = tlg.split('|')[1]
    except:
        token = ""
        id = ""
# telegram Post


def sndToTelegram(id, token, mesg):
    r = requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={mesg}')

# driver runner


def driver(path):
    options = webdriver.ChromeOptions()
    #PROXY = '193.30.243.175:8080'
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--disable-blink-features=AutomationControlled')
    #options.add_argument('--proxy-server=%s' % PROXY)
    drv = webdriver.Chrome(
        options=options, executable_path=path)
    return drv


# banner

def banner(hits, inv, chk):
    return f'''{colors.bold} 
  {colors.R} 
::::    ::: :::::::::: ::::::::::: :::::::::: :::        ::::::::::: :::    ::: 
:+:+:   :+: :+:            :+:     :+:        :+:            :+:     :+:    :+: 
:+:+:+  +:+ +:+            +:+     +:+        +:+            +:+      +:+  +:+  
+#+ +:+ +#+ +#++:++#       +#+     :#::+::#   +#+            +#+       +#++:+   
+#+  +#+#+# +#+            +#+     +#+        +#+            +#+      +#+  +#+  
#+#   #+#+# #+#            #+#     #+#        #+#            #+#     #+#    #+# 
###    #### ##########     ###     ###        ########## ########### ###    ### 

        {colors.B}NETFLIX CHECKER V 1.0.0  selenium  by nouredinekn
        {colors.W}------------------------------------------------------------------------------------------------------------                                                                 
        {colors.bold} {colors.Y} [ {colors.R}! {colors.Y}] {colors.P} DEV BY:  {colors.G} NOUREDINE KN 
        {colors.bold} {colors.Y} [ {colors.R}! {colors.Y}] {colors.P}TG-USER:  {colors.G} t.me/n2k4n
        {colors.bold}{colors.Y} [ {colors.R}! {colors.Y}] {colors.P}github: {colors.G}  github.com/nouredinekn
        {colors.bold}{colors.Y} [ {colors.R}! {colors.Y}] {colors.P}DATE: {colors.G}{datetime.datetime.now().date()}
        {colors.W}------------------------------------------------------------------------------------------------------------
        {colors.P} CHECKED: {chk}
        {colors.R} INVALIDE: {inv}
        {colors.G} HITS:    {hits}
'''
# copyRight c


def other():
    return 'Nouredine_Kn | @n2k4n '
