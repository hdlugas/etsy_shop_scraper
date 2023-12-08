library(ggplot2)
library(ggcorrplot)
library(dplyr)

#import processed data
df = read.csv(file='~/etsy_shop_scraper/final_processed_data.csv')

#drop shop_name and shop_id columns
df = df %>% select(-shop_name)
df = df %>% select(-shop_id)


#create correlation matrix
ggcorrplot(cor(df))


#change rating from 7 levels to 4 levels and encode as factor variable
df$avg_rating[which(df$avg_rating <= 3.5)] = 0
df$avg_rating[which(df$avg_rating == 4.5)] = 4
df$avg_rating = factor(df$avg_rating, levels = c('0','4','5'), labels = c('<4', '4-5', '5'))


#distribution of rating
ggplot(df, aes(x=avg_rating)) +  geom_bar() + ggtitle('Distribution of Shop Rating') + 
  theme(plot.title = element_text(hjust = 0.5, size=24), panel.background=element_blank(), 
        panel.border = element_rect(color="black", fill=NA, linewidth=0.3),
        axis.title=element_text(size=24))  +
  ylim(0,1200) +
  xlab('Average Rating') + ylab('Count')


#stacked histograms of various predictor variables grouped by rating
ggplot(df, aes(x=factor(accepts_custom_requests,levels=c(0,1),labels=c('No','Yes')), fill = as.factor(avg_rating))) +
  geom_histogram(stat = 'count') + 
  ggtitle('Custom Requests Flag Distribution\n by Average Rating') +
  theme(plot.title = element_text(hjust = 0.5, size=24), panel.background=element_blank(), 
        panel.border = element_rect(color="black", fill=NA, linewidth=0.3),
        axis.title=element_text(size=24))  +
  # scale_x_continuous(limits = c(0,400)) +
  xlab('Accepts Custom Requests') + ylab('Count') + labs(fill = 'Average Rating')

ggplot(df, aes(x=number_items_listed, fill = as.factor(avg_rating))) + geom_histogram(binwidth=10) + 
  ggtitle('Number of Items Listed\n Distribution by Average Rating') +
  theme(plot.title = element_text(hjust = 0.5, size=24), panel.background=element_blank(), 
        panel.border = element_rect(color="black", fill=NA, linewidth=0.3),
        axis.title=element_text(size=24))  +
  scale_x_continuous(limits = c(0,320)) +
  scale_y_continuous(limits = c(0,300)) +
  xlab('Number of Items Listed') + ylab('Count') + labs(fill = 'Average Rating')

ggplot(df, aes(x=avg_price, fill = as.factor(avg_rating))) + geom_histogram(binwidth=100) + 
  ggtitle('Average Item Price\n Distribution by Average Rating') +
  theme(plot.title = element_text(hjust = 0.5, size=24), panel.background=element_blank(), 
        panel.border = element_rect(color="black", fill=NA, linewidth=0.3),
        axis.title=element_text(size=24))  +
  scale_x_continuous(limits = c(0,1100)) +
  xlab('Average Price') + ylab('Count') + labs(fill = 'Average Rating')

df$number_feature_items = factor(df$number_feature_items,levels=c(0,1,2,3,4))
df = df[which(is.na(df$number_feature_items) == FALSE),]
ggplot(df, aes(x=number_feature_items, fill = as.factor(avg_rating))) + 
  geom_histogram(stat = 'count') + 
  ggtitle('Number of Feature Items\n Distribution by Average Rating') +
  theme(plot.title = element_text(hjust = 0.5, size=24), panel.background=element_blank(), 
        panel.border = element_rect(color="black", fill=NA, linewidth=0.3),
        axis.title=element_text(size=24))  +
  # scale_x_continuous(limits = c(0,1100)) +
  xlab('Number of Feature Items') + ylab('Count') + labs(fill = 'Average Rating')









