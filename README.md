# etsy_shop_scraper
This repo contains a script that scrapes Etsy shops using Beautiful Soup and another script which further processes the data.

The script 'shop_scraper.py':
1. inputs i) a keyword that is searched in the Etsy shop search engine and ii) the total number of pages (each page has 10 shops, at least as of 11/2022) to be scraped.
2. writes a csv which has one row for each Etsy shop scraped and columns ['shop_name', 'shop_id', 'accepts_custom_requests', 'number_admirers', 'total_sales', 'starting_year', 'number_reviews', 'avg_rating', 'number_items_listed', 'avg_price', 'std_price', 'avg_feat_price', 'std_feat_price', 'number_feature_items', 'sales_per_year'] to a path that you must change. 

The script 'processing.py':
1. removes rows that have NaN for avg_rating.
2. removes columns that have the same constant value for all observations.
3. replace 't' and 'f' entries with '1' and '0' in 'accepts_custom_requests' predictor column, respectively.
4. imputes NaN entries using K-Nearest Neighbors with K=5.
5. creates new predictor column 'sales_per_year'.
6. writes processed dataframe to csv.
