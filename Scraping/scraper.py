import requests
from bs4 import BeautifulSoup
import csv

# fetch the web page
page = requests.get('https://the-coding-pie.github.io/top_movies/')


soup = BeautifulSoup(page.content, 'lxml')

titles = []
for h3 in soup.find_all('h3'):
  titles.append(h3.string.strip())

# genres
genres = []
for genre in soup.find_all('p', class_='genre'):
  genres.append(genre.string.strip())


""" scraping using css_selector eg: select('span.class_name') """
# ratings, selecting all span with class="rating"
ratings = []
for rating in soup.select('span.rating'):
  ratings.append(rating.string.strip())

# lengths, selecting all span with class="length"
lengths = []
for length in soup.select('span.length'):
  lengths.append(length.string.strip())

# years, selecting all span with class="year"
years = []
for year in soup.select('span.year'):
  years.append(year.string.strip())


""" scraping by navigating through elements eg: div.span.string """
# budget
budgets = []
for budget in soup.find_all('div', class_='budget'):
  # from <div class="budget"></div>, get the span.string
  budgets.append(budget.span.string.strip())

# gross
grosses = []
for gross in soup.find_all('div', class_='gross'):
  grosses.append(gross.span.string.strip())


""" parsing all the "src" attribute's value of <img /> tag """
img_urls = []
for img in soup.find_all('img', class_='poster'):
  img_urls.append(img.get('src').strip())


""" writing data to CSV """

# open top25.csv file in "write" mode
with open('top25.csv', 'w') as file:
  # create a "writer" object
  writer = csv.writer(file, delimiter=',')

  # use "writer" obj to write
  # you should give a "list"
  writer.writerow(["title", "genre", "ratings", "length", "year", "budget", "gross", "img_url"])

  for i in range(25):
    writer.writerow([
      titles[i],
      genres[i],
      ratings[i],
      lengths[i],
      years[i],
      budgets[i],
      grosses[i],
      img_urls[i]
    ])