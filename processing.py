import pandas as pd
from sklearn.impute import KNNImputer

#set pandas display options
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#import scraped data
df1 = pd.read_csv('~/STA6840/final_project/data/etsy_woodshop_data1-60.csv')
df2 = pd.read_csv('~/STA6840/final_project/data/etsy_woodshop_data62-96.csv')
df3 = pd.read_csv('~/STA6840/final_project/data/etsy_woodshop_data98-199.csv')
df4 = pd.read_csv('~/STA6840/final_project/data/etsy_woodshop_data200-299.csv')
df5 = pd.read_csv('~/STA6840/final_project/data/etsy_woodshop_data300-399.csv')
df6 = pd.read_csv('~/STA6840/final_project/data/etsy_woodshop_data400-493.csv')


#merge the dataframes into one dataframe and drop duplicates
df = pd.concat([df1, df2, df3, df4, df5, df6]).sort_index().drop_duplicates(subset=['shop_id'], keep='first')

#drop rows that have NaN for average rating
df = df.dropna(subset=['avg_rating'])

#drop extraneous column
df = df.drop('Unnamed: 0', axis=1)

#drop columns that have the same entry for all rows
for col in df.columns.tolist():
    if len(df[col].unique()) == 1:
        df = df.drop([col], axis=1)

#replace t and f flags in 'accepts_custom_requests' with 1 and 0, respectively
df['accepts_custom_requests'].loc[df['accepts_custom_requests'] == 't'] = 1
df['accepts_custom_requests'].loc[df['accepts_custom_requests'] == 'f'] = 0


#Impute NaN entries using K-nearest neighbors with K=4
#list of columns to not use in the KNN imputationimpute
non_imputed_cols = ['shop_name', 'shop_id']

#create an object for KNNImputer
imputer = KNNImputer(n_neighbors=3)
imputed_df = pd.DataFrame(imputer.fit_transform(df.drop(non_imputed_cols, axis=1)), columns=df.drop(non_imputed_cols, axis=1).columns)

#merge the columns used in KNN imputation with those not used in KNN imputation
merged_df = pd.concat([df[non_imputed_cols].reset_index(), imputed_df.reset_index()], axis=1, join='inner').drop('index', axis=1)

#create new predictor column of sales per unit time
merged_df['sales_per_year'] = merged_df['total_sales'] / (2023- merged_df['starting_year'])

merged_df.to_csv('~/STA6840/final_project/data/final_processed_data.csv', index=False)

