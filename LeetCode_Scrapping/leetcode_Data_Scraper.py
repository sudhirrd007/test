import requests
from bs4 import BeautifulSoup
import pandas as pd


# copy source code of webpage from chrome browser
file = open("leetcode.html", "rb")

html = file.read()

file.close()

# initilize soup object
soup = BeautifulSoup(html, "lxml")

# fetch table
tableBody = soup.find("tbody", class_="reactable-data")

# fetch all <tr> tages
tr_s = tableBody.find_all("tr")

# problem number
numbers = [td.find("td", attrs={"label":"#"}).string for td in tr_s]

# problem title
titles = [td.find("td", attrs={"label": "Title"})["value"] for td in tr_s]

suffix = "https://leetcode.com"
# problem leetcode link
links = [suffix + td.find("td", attrs={"label": "Title"}).div.a["href"] for td in tr_s]

# acceptance rate of problem
accept_rate = [td.find("td", attrs={"label": "Acceptance"})["value"] for td in tr_s]
accept_rate = [round(float(acc[:6]), 2) for acc in accept_rate]
accept_rate = [str(acc)+"%" for acc in accept_rate]

# difficulty level (EASY, MEDIUM and HARD)
difficulty = [td.find("td", attrs={"label": "Difficulty"}).span.string.upper() for td in tr_s]


columns = ["#", "Title", "Difficulty", "Acceptance rate", "LeetCode Link"]
df = pd.DataFrame(columns=columns)

df["#"] = numbers
df["Title"] = titles
df["Difficulty"] = difficulty
df["Acceptance rate"] = accept_rate
df["LeetCode Link"] = links

# export to csv file
df.to_csv("leetcodeDataSet.csv", index=False)