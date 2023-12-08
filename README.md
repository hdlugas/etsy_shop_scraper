# Etsy Shop Scraper
This repository contains a python script that scrapes Etsy shops using the Beautiful Soup library and a python script which processes the data.

The script 'shop_scraper.py':
1. inputs i) a keyword that is searched in the Etsy shop search engine and ii) the total number of pages (each page has 10 shops as of 11/2022) to be scraped.
2. writes a csv which has one row for each Etsy shop scraped and columns ['shop_name', 'shop_id', 'currency_id', 'country_id', 'listing_enabled', 'browsing_enabled', 'buyer_location_restricted', 'rate_updated_enabled', 'test_account', 'accepts_custom_requests', 'number_admirers', 'total_sales', 'starting_year', 'number_reviews', 'avg_rating', 'number_items_listed', 'avg_price', 'std_price', 'avg_feat_price', 'std_feat_price', 'number_feature_items'] to a path that you must change. 

<br />
<br />
<br />

The script 'processing.py' inputs the output csv file from the script 'shop_scraper.py' and:
1. removes rows that have NaN for avg_rating.
2. removes columns that have the same constant value for all observations.
3. replace 't' and 'f' entries with '1' and '0' in 'accepts_custom_requests' column, respectively.
4. imputes NaN entries using K-Nearest Neighbors with K=5.
5. creates new predictor column 'sales_per_year'.
6. writes processed dataframe to csv.

<br />
<br />
<br />

The script 'visuals.R' inputs the output csv file from the script 'processing.py' and generates figures of:
1. the correlation matrix of the processed data frame.<br />
<img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/a83a5754-cdf2-4cd3-bbfe-cb20096dac0a" width="600" /> <br />

2. the distribution of a given variable (taken here to be shop rating).<br />
<img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/102dae69-5349-408e-8e05-0f1540d86c4d" width="600" /> <br />

3. the distribution of the response variable grouped by a given predictor variable (in this case, the response variable is shop rating and the predictor variables are number of shop admirers and a flag indicating whether the shop accepts custom requests)<br />
<p float="left">
  <img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/00eeb75a-fc40-4267-a5fe-7f812dc6495e" width="400" />
  <img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/120c3b8a-b557-4e5d-98a5-04d93cec85e5" width="400" />  
  <img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/f1a642a0-ec7f-4337-b389-c295320a2626" width="400" />
  <img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/8d400dae-df5c-4391-bc60-a0b693f7588f" width="400" />
</p>

