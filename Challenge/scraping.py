## Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt
import pandas as pd


def scrape_all():

    ## Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(browser),
      "hemispheres":hemispheres(browser),
      "last_modified": dt.datetime.now()
    }

     # Stop webdriver and return data
    browser.quit()
    return data



def mars_news(browser):

    ## Scraping Mission to Mars Data
    url = 'https://redplanetscience.com'
    browser.visit(url)
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    ### Title and Summary

    # Parse the HTML
    html = browser.html
    news_soup = soup(html,'html.parser')

    try: 
        slide_elem = news_soup.select_one('div.list_text')

        news_title = slide_elem.find('div',class_='content_title').get_text()
        news_title

        news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
        news_p

    except AttributeError:
        return None, None

    return news_title, news_p



### Featured Image

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    html = browser.html
    img_soup = soup(html,'html.parser')

    try:
        img_url_rel = img_soup.find('img',class_='fancybox-image').get('src')
        img_url_rel

    except AttributeError:
        return None

    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url


### Mars Facts

def mars_facts(browser):

    try: 
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    
    except BaseException:
        return None
    
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    return df.to_html()



### Hemispheres Images and titles 

def hemispheres(browser):

    # Visit the URL
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Convert browser HTML into Beautiful Soup object 
    html = browser.html
    soup_object = soup(html,'html.parser')

    # Create a list to hold images and titles
    hemisphere_image_urls = []

    # Write code to retrieve the image urls and titles for each hemisphere.
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
        

    # Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls
    print(hemisphere_image_urls)


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())




