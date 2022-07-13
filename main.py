import requests
import time
from time import sleep
from pprint import pprint
from bs4 import BeautifulSoup
import html
import pandas
import datetime
from datetime import date
from time import sleep
import csv
class StackOwerflow:
    counter = 0
    list = []
    n = int(input("Какой период вас интересует? (дни назад) :"))
    print("Например: git, python, java, php, android и т.д.")
    tag = input("Введите нужный вам тэг: ")


    def timer(self):
        self.count_of_page = 0
        for page in range(1, 1000):
            print(f"Обработка {page} страницы")
            url = f"https://stackoverflow.com/questions/tagged/{self.tag}?tab=newest&page={page}&pagesize=50"
            r = requests.get(url)
            sleep(1)
            soup = BeautifulSoup(r.text, "html.parser")
            self.count_of_page += 1
            times = soup.findAll("span", class_="relativetime")
            today = date.today() - datetime.timedelta(days=self.n)

            for time in times:
                time_title = time.get("title")
                time_srez = time_title[0:10].replace("-", "")
                time_year = int(time_srez[0:4])
                time_month = int(time_srez[4:6])
                time_day = int(time_srez[6:8])
                period = datetime.date(time_year, time_month,time_day)
                self.counter += 1
                if period <= today:
                    print(f"Обрабатываю статьи до {period} числа")
                    return self.counter
    def stack(self):
        self.title_counter = 0
        not_full_url = "https://stackoverflow.com"
        for page in range(0, self.count_of_page):
            url = f"https://stackoverflow.com/questions/tagged/{self.tag}?tab=newest&page={page}&pagesize=50"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            links = soup.findAll("a", class_="s-link")
            for link in links:
                title = link.text
                all_link = not_full_url + link.get("href")
                if "https://stackoverflow.com/questions" in all_link:
                    new_list = []
                    new_list.append(title)
                    new_list.append(all_link)
                    self.list.append(new_list)
                    self.title_counter += 1
                    if self.title_counter == self.counter:
                        return pprint(f"Всего найдено {len(self.list)} статьи")
    def csv(self):
        print("Преобразую в базу данных")
        sleep(3)
        pandas.set_option("display.max_rows", None)
        header = ["Заголовок", "Ссылка"]
        df = pandas.DataFrame(self.list, columns=header)
        df.to_csv("data.csv", index=False, header =False)
        print(df)
if __name__ == '__main__':
    s = StackOwerflow
    s.timer(s)
    s.stack(s)
    s.csv(s)