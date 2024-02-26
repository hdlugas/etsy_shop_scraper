# Etsy Shop Scraper
The script 'shop_scraper.py':
1. inputs i) a keyword that is searched in the Etsy shop search engine and ii) the total number of pages (each page has 10 shops as of 11/2022) to be scraped.
2. writes a csv which has one row for each Etsy shop scraped and columns ['shop_name', 'shop_id', 'currency_id', 'country_id', 'listing_enabled', 'browsing_enabled', 'buyer_location_restricted', 'rate_updated_enabled', 'test_account', 'accepts_custom_requests', 'number_admirers', 'total_sales', 'starting_year', 'number_reviews', 'avg_rating', 'number_items_listed', 'avg_price', 'std_price', 'avg_feat_price', 'std_feat_price', 'number_feature_items'] to a csv file located at a path that you must change. 

<br />

The correlation matrix of the processed data frame:<br />
<img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/9e5b348a-67ac-4393-a029-e57a375d54ed" width="600" /> <br />

The distribution of a given variable (taken here to be shop rating):<br />
<img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/102dae69-5349-408e-8e05-0f1540d86c4d" width="600" /> <br />

The distribution of a given variable (e.g. accepts custom requests flag, number of items listed, average item price, number of feature items) grouped by a given categorical variable (e.g. average shop rating): <br />
<img src="https://github.com/hdlugas/etsy_shop_scraper/assets/73852653/ed2d35a4-3e59-498b-8ca8-47b98e552ec4" width="800" /> <br />



