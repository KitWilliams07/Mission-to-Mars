# Mission-to-Mars

In this repository, the main goal was utilize HTML and webscraping to pull up to date data on the Mission to Mars. Then to compile this information in an easy to read webpage format as well as storing any neccesary data in MongoDB.

First, jupyter notebook file (Mission_to_Mars_Challenge.ipynb) was created to scrape all the neccesary data from the internet. This included gathering titles, tables, and image links. The python "splinter" package was utilize to automate the webscraping process. Splinter allowed me to create a script that visited the neccesary webpage and traverse around each one to locate the information needed, such as the link to full size images rather than the ones displayed on the website's homepage. This file was then converted to a .py file (Mission_to_Mars_Challenge.py) in order to be compatible with the rest of the packages used in this project.

Once all of the data was scraped, the python "Flask" package was used to generate a webpage to display all of this data. The Flask webpage was created in the app.py file. Within this file, it connects to our MongoDB database which is used to store all of the scraped data. The app.py file is also linked to an html file (index.html) which provides the setup to the webpage. Additionally, in order to provide clean and easy to read code, all of the scraping functions are contained within an additional document. This gives the app.py the ability to scrape all of the neccesary data, which is linked to a button in the html file. 

Overall this repo creates an easy to read resource for information on the most up to date news on humanities "Mission to Mars".
