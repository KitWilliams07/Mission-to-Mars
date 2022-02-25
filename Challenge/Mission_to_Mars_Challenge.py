
# Import Splinter, Beautiful Soup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


### Scraping Mission to Mars Data

# Visit Mars News Site
url = 'https://redplanetscience.com'
browser.visit(url)
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser HTML into soup object
html = browser.html
news_soup = soup(html,'html.parser')
slide_elem = news_soup.select_one('div.list_text')


### Title and Summary

# Grab the title of the most recent news article
news_title = slide_elem.find('div',class_='content_title').get_text()
news_title

# Grab the summary of this article
news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
news_p


### Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Click on the full size image
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem
full_image_elem.click()

# Convert the browswer HTML into Beautiful soup object
html = browser.html
img_soup = soup(html,'html.parser')


# Grab full size image url 
img_url_rel = img_soup.find('img',class_='fancybox-image').get('src')
img_url_rel

# Combine with homepage url for full URL 
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


### Mars Facts

# Use pandas to read in HTML table 
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()


### D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# 1. Visit the URL
url = 'https://marshemispheres.com/'
browser.visit(url)

# Convert browser HTML into Beautiful Soup object 
html = browser.html
soup_object = soup(html,'html.parser')

# 2. Create a list to hold images and titles
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
results = soup_object.find('div',class_='collapsible results')
items = results.find_all('div',class_='item')

hemisphere_image_urls = []

for item in items:
    hemispheres ={}
    
    link = item.find('a',class_='itemLink product-item').get('href')
    full_link = 'https://marshemispheres.com/'+link
    browser.visit(full_link)
    
    new_html = browser.html
    new_page_soup_object = soup(new_html,'html.parser')
    full_res = new_page_soup_object.find('div',class_='downloads').find('a').get('href')
    img_url = 'https://marshemispheres.com/'+full_res
    
    hemispheres['img_url'] = img_url
    
    img_name = new_page_soup_object.find('div',class_='cover').find('h2').text
    
    hemispheres['title'] = img_name
    hemisphere_image_urls.append(hemispheres)
    

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()



