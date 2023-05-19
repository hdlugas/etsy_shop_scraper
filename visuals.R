library(ggplot2)
library(ggcorrplot)
library(grid)
library(vcd)
library(dplyr)

#import processed data
df = read.csv(file='~/STA6840/final_project/data/final_processed_data.csv')

#drop shop_name and shop_id columns
df = df %>% select(-shop_name)
df = df %>% select(-shop_id)

#create correlation matrix
ggcorrplot(cor(df))

#change rating from 7 levels to 4 levels and encode as factor variable
df$avg_rating[which(df$avg_rating <= 3.5)] = 0
df$avg_rating[which(df$avg_rating == 4.5)] = 4
df$avg_rating = as.factor(df$avg_rating)


#distribution of rating
ggplot(df, aes(x=avg_rating)) +  geom_bar() + ggtitle('Distribution of Shop Ratings') + 
  theme(plot.title = element_text(hjust = 0.5, size=24)) + theme(axis.title=element_text(size=24))


#stacked histograms of various predictor variables grouped by rating
ggplot(df, aes(x=number_admirers, fill = as.factor(avg_rating))) + geom_histogram(binwidth=100) + ggtitle('Stacked Histogram') +
  theme(plot.title = element_text(hjust = 0.5, size=28)) + theme(axis.title=element_text(size=24))

ggplot(df, aes(x=accepts_custom_requests, fill = as.factor(avg_rating))) + geom_histogram(binwidth=0.5) + ggtitle('Stacked Histogram') +
  theme(plot.title = element_text(hjust = 0.5, size=28)) + theme(axis.title=element_text(size=24))

ggplot(df, aes(x=number_items_listed, fill = as.factor(avg_rating))) + geom_histogram(binwidth=75) + ggtitle('Stacked Histogram') +
  theme(plot.title = element_text(hjust = 0.5, size=28)) + theme(axis.title=element_text(size=24))

ggplot(df, aes(x=number_feature_items, fill = as.factor(avg_rating))) + geom_histogram(binwidth=1) + ggtitle('Stacked Histogram') +
  theme(plot.title = element_text(hjust = 0.5, size=28)) + theme(axis.title=element_text(size=24))

ggplot(df, aes(x=sales_per_year, fill = as.factor(avg_rating))) + geom_histogram(binwidth=250) + ggtitle('Stacked Histogram') +
  theme(plot.title = element_text(hjust = 0.5, size=28)) + theme(axis.title=element_text(size=24))

ggplot(df, aes(x=avg_price, fill = as.factor(avg_rating))) + geom_histogram(binwidth=100) + ggtitle('Stacked Histogram') +
  theme(plot.title = element_text(hjust = 0.5, size=28)) + theme(axis.title=element_text(size=24))










