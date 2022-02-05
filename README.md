# Web Scraper

This project is made in pyhthon.
It took some info. from website list then add them into data.json file.

The dependencies used are:
>request

>bs4

Algorithm:

The csv file opened,
csv reader module is imported and file is opened.

A header array is made and the header values are added.

Row was accessed using loop, url oepned and values of country and asin are inserted according to the loop.

By using BeautifulSoup we took the html code and got the raequired information, the informations are added in a json file (data.json)
