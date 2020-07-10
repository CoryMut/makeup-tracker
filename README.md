# makeup-tracker

The purpose of this project was to create a place to keep track of your makeup! 
Makeup is a large industry and some people can end up with some pretty large collections, but there was not a convenient place to sort or track it all.

The data (encompassing over 17,000 products) is largely from Ulta, with the hope of adding Sephora in the future.

The name, brand, color, type, category, and price are all collected for each product.

The project can be found at: https://makeup-tracker.herokuapp.com/


To reduce the number of times Ulta's servers are pinged, copies of the data are saved in the case of errors. This means Ulta's servers are only requested once per item, and only if the item has never been requested before. Additionally, the html is updated as more products are added, allowing for an easy way to seed another database that is just as up to date as the other.
