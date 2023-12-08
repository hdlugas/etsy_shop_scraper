# Etsy Shop Scraper
This repository contains three python scripts: one that scrapes Etsy shops using the Beautiful Soup library, one that processes the scraped data, and one that produces some figures of the processed data.

The script 'shop_scraper.py':
1. inputs i) a keyword that is searched in the Etsy shop search engine and ii) the total number of pages (each page has 10 shops as of 11/2022) to be scraped.
2. writes a csv which has one row for each Etsy shop scraped and columns ['shop_name', 'shop_id', 'currency_id', 'country_id', 'listing_enabled', 'browsing_enabled', 'buyer_location_restricted', 'rate_updated_enabled', 'test_account', 'accepts_custom_requests', 'number_admirers', 'total_sales', 'starting_year', 'number_reviews', 'avg_rating', 'number_items_listed', 'avg_price', 'std_price', 'avg_feat_price', 'std_feat_price', 'number_feature_items'] to a csv file located at a path that you must change. 

<br />
<br />

The script 'processing.py' inputs the csv file of scraped data from the script 'shop_scraper.py' and:
1. removes rows that have NaN for avg_rating.
2. removes columns that have the same constant value for all observations.
3. replace 't' and 'f' entries with '1' and '0' in 'accepts_custom_requests' column, respectively.
4. imputes NaN entries using K-Nearest Neighbors with K=5.
5. creates new predictor column 'sales_per_year'.
6. writes processed dataframe to csv.

<br />
<br />

The script 'visuals.R' inputs the output csv file from the script 'processing.py' and generates figures of:
1. the correlation matrix of the processed data frame.<br />
<img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/a83a5754-cdf2-4cd3-bbfe-cb20096dac0a" width="600" /> <br />

2. the distribution of a given variable (taken here to be shop rating).<br />
<img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/102dae69-5349-408e-8e05-0f1540d86c4d" width="600" /> <br />

3. the distribution of a given variable (e.g. accepts custom requests flag, number of items listed, average item price, number of feature items) grouped by a given categorical variable (e.g. average shop rating) <br />
<img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/ed2d35a4-3e59-498b-8ca8-47b98e552ec4" width="800" /> <br />



