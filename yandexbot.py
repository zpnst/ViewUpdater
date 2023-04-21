import os
import sys
import time
import random
import multiprocessing
from datetime import datetime
from selenium import webdriver
from collections import Counter
from multiprocessing import Pool 
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService





path = "linksfolder"
useragent = UserAgent
driver_path = os.path.abspath("driver\\geckodriver.exe")

_useragentslist = open("sources\\useragents.txt").readlines()
useragentslist = [x.strip() for x in _useragentslist]
random_index = random.randrange(len(useragentslist))
randomuserragent = useragentslist[random_index]

url = "https://yandex.ru"
location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

service = Service(executable_path=driver_path, log_path='nul')

options = webdriver.FirefoxOptions()  
#options.add_argument('-headless')
options.add_argument(f"user-agent={useragent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--log-level=3')
options.binary_location=location

def randomize(path):


    all = [] 
    
    contents = os.listdir(path)

    for content in contents:

        _tools = open(f"{path}\\{content}").readlines()
        all.append([x.strip() for x in _tools])

    tools = [x for l in all for x in l]

    rand_tools = random.sample(tools, len(tools))

    return rand_tools

def cleaner(urls):

    val = []
    result = []

    len_urls = [len(x) for x in urls]

    cnt_urls = Counter(urls)
    set_urls = set(urls)

    cnt_len_urls = Counter(len_urls)
    set_len_urls = set(len_urls)

    
    for values in dict(cnt_len_urls).values():

        val.append(values)

    max_val = max(val)

    for key, value in dict(cnt_len_urls).items():

        if value == max_val:

            curr_key = key

    for url in urls:

        if len(url) == curr_key:

            result.append(url)

    return result

def mainest(links, kount):

    links_bunches = []

    for link in range(0, len(links) - (kount-1), kount):

        if kount == 5:
            links_bunches.append([links[link], links[link+1], links[link+2], links[link+3], links[link+4]])
        if kount == 4:
            links_bunches.append([links[link], links[link+1], links[link+2], links[link+3]])
        if kount == 3:
            links_bunches.append([links[link], links[link+1], links[link+2]])
        if kount == 2:
            links_bunches.append([links[link], links[link+1]])
        if kount == 1:
            links_bunches.append([links[link]])

    if len(links)%kount != 0:

        links_bunches += [links[(len(links)-len(links)%kount):]]

    else:

        pass

    return links_bunches

def elements(element):

    if element.is_enabled() == True:

        element.click()

    else: 

        pass

def get_data(url):


    try:

        driver = webdriver.Chrome(
        options=options, 
        service=service
        )

        driver.get(url=url)
        time.sleep(random.randint(14, 23))
        

    except Exception as exs:
        print(exs)

    finally: 

        time.sleep(random.randint(14, 23))
        driver.close()
        driver.quit()

def begining(kount):

    rand_tools = randomize(path)
    links = cleaner(rand_tools)
    
    links_bunches = mainest(links, kount)

    links_kount = 0
    for link_bunch in links_bunches:
    
        if len(link_bunch) == 5:
            print(f"""
            ВРЕМЯ - [{str(datetime.now().time())[:8]}], ДАННЫЕ ССЫЛКИ НАХОДЯТСЯ В РАБОТЕ:

            1)Cсылка - {link_bunch[0]}
            2)Cсылка - {link_bunch[1]}
            3)Cсылка - {link_bunch[2]}
            4)Cсылка - {link_bunch[3]}
            5)Ссылка - {link_bunch[4]} 

            ОБРАБОТАННО {links_kount} ИЗ {len(links)} ССЫЛОК
            """)
        if len(link_bunch) == 4:
            print(f"""
            ВРЕМЯ - [{str(datetime.now().time())[:8]}], ДАННЫЕ ССЫЛКИ НАХОДЯТСЯ В РАБОТЕ:

            1)Cсылка - {link_bunch[0]}
            2)Cсылка - {link_bunch[1]}
            3)Cсылка - {link_bunch[2]}
            4)Cсылка - {link_bunch[3]} 

            ОБРАБОТАННО {links_kount} ИЗ {len(links)} ССЫЛОК
            """)
        if len(link_bunch) == 3:
            print(f"""
            ВРЕМЯ - [{str(datetime.now().time())[:8]}], ДАННЫЕ ССЫЛКИ НАХОДЯТСЯ В РАБОТЕ:

            1)Cсылка - {link_bunch[0]}
            2)Cсылка - {link_bunch[1]}
            3)Cсылка - {link_bunch[2]}

            ОБРАБОТАННО {links_kount} ИЗ {len(links)} ССЫЛОК
            """)
        if len(link_bunch) == 2:
            print(f"""
            ВРЕМЯ - [{str(datetime.now().time())[:8]}], ДАННЫЕ ССЫЛКИ НАХОДЯТСЯ В РАБОТЕ:

            1)Cсылка - {link_bunch[0]}
            2)Cсылка - {link_bunch[1]} 

            ОБРАБОТАННО {links_kount} ИЗ {len(links)} ССЫЛОК
            """)
        if len(link_bunch) == 1:
            print(f"""
            ВРЕМЯ - [{str(datetime.now().time())[:8]}], ДАННАЯ ССЫЛКА НАХОДИТСЯ В РАБОТЕ:

            1)Cсылка - {link_bunch[0]}

            ОБРАБОТАННО {links_kount} ИЗ {len(links)} ССЫЛОК
            """)

        links_kount  += len(link_bunch)

        process_count = len(link_bunch)
        poo = Pool(processes=process_count)
        poo.map(get_data, link_bunch)

    end = input(f"ПРОГРАММА ОБОШЛА ВСЕ ЗАГРУЖЕННЫЕ ССЫЛКИ ({links_kount} шт) =)\nДля завершения программы нажмите на Enter: ")
    if end == "":
        
        time.sleep(2)
        sys.exit()
        

def starting():
        
    print("\nНАСТРОЙКИ РАБОТЫ ПРОГРАММЫ: \n")

    links_kount = input("Введите количество окон(цифра от 1 до 5), которое бдует открываться за одну прокрутку: ")

    if links_kount == "1" or links_kount == "2" or links_kount == "3" or links_kount == "4" or links_kount == "5" or links_kount == "6" or links_kount == "7":
            
            start = input("\nЧтобы начать нажмите на Enter: ")

            if start.lower() == "":

                begining(int(links_kount))
    else:
        print("""Вы ввели не то число, пройдите настройку заново. 
На это шаге, вам нужно было ввести цифру от 1 до 5, это в целях безопасности вашего компьютера=)""")
        starting()


def main ():

    try:
        
        starting()

    except Exception as e:

        print(f"\nОШИБКА: {e}")

        exception = input("\nПрограмма выдала ошибку. \nПроверьте, добавили ли вы файлы с ссылками в папку 'linksfolder'"\
            "\nИли же проверьте подключение к интернету. \nПосле этого перезапустите программу:)\n\nЧтобы завершить программу нажмите на Enter: ")
        
        if exception == "":
            time.sleep(2)
            sys.exit()

if __name__ == "__main__":
    
    multiprocessing.freeze_support()
    main()