# makeup-tracker

The purpose of this project was to create a place to keep track of your makeup! 
Makeup is a large industry and some people can end up with some pretty large collections, but there was not a convenient place to sort or track it all.

The data (encompassing over 17,000 products) is largely from Ulta, with the hope of adding Sephora in the future.

The name, brand, color, type, category, and price are all collected for each product.

Formerly hosted on Heroku before they axed free accounts. Looking for a new host.


To reduce the number of times Ulta's servers are pinged, copies of the data are saved in the case of errors. This means Ulta's servers are only requested once per item, and only if the item has never been requested before. Additionally, the html is updated as more products are added, allowing for an easy way to seed another database that is just as up to date as the other.

A large part of this project was obtaining the data and making it automated. This is where I learned the most and spent the most time, but it still is not perfect. However, the final product is totally functional on heroku. Currently, users can make an account and start searching for products to add to their collection immediately. Each collection is private, but support for whether you want to make it public or only visible to those with the link (google docs style) will come later. Each collection can be filtered by brand, category (such as eyes, face, or lips), and by type (such as eyeliner).

Support for more than one collection will come later with the idea that people will be able to share recommended products quickly and in one place to their friends, clients, or anyone!

Project was completed using:
* Javascript
* Python
* Flask/jinja2
* beautifulsoup4
