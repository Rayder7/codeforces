import csv
from time import sleep

import requests
from bs4 import BeautifulSoup

url = "https://codeforces.com/problemset?order=BY_SOLVED_DESC&locale=ru"

headers = {
    "Accept": "*/*",
}

req = requests.get(url, headers=headers)
src = req.text

with open("index.html", "w", encoding="utf-8-sig") as file:
    file.write(src)

with open("index.html", encoding="utf-8-sig") as file:
    src = file.read()


def parser():
    soup = BeautifulSoup(src, "lxml")

    all_problems = soup.find(class_="problems").find_all("tr")
    d = 0
    for item in all_problems:
        if d == 0:
            d += 1

            continue
        number = item.find_all(class_="id")
        for i in range(len(number)):
            number = number[i].text.strip()

        name = item.find(style="float: left;").text.strip()

        groups = item.find(
            style="float: right; font-size: 1.1rem; padding-top: 1px; text-align: right;").text
        groups = groups.replace(',', '').split()

        rating = item.find(class_="ProblemRating").text

        count_vin = item.find(title="Количество решивших задачу").text
        count_vin = count_vin[2:]

        with open(("data.csv"), "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    number,
                    name,
                    groups,
                    rating,
                    count_vin
                )
            )


def main():
    parser()


if __name__ == '__main__':
    main()
