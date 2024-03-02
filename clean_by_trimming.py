# import pandas & seaborn library
import pandas as pd
import seaborn as sns


class clean1 :
    
    @staticmethod
    
    def trim_process(df,col_name):
        
        # check your column is exists or not in your dataframe
        
        if col_name in df.columns:
            
            column_data = df[col_name]
            
            #using outlier remove by manually method
            
            Q1 = df[col_name].quantile(25/100)
            Q2 = df[col_name].quantile(50/100)
            Q3 = df[col_name].quantile(75/100)
            
            # counting Initial Quartile Range
            IQR = Q3-Q1
            
            lower_limit = Q1 - (1.5*IQR)
            upper_limit = Q3 + (1.5*IQR)
            
            data1 = df[(df[col_name]>=lower_limit)  & (df[col_name]<=upper_limit)]
            
            
            # showing result from calculate by manually method
            print("~> Data before cleaning outliers within the data : " ,len(df))
            print("~> Number of outliers within the data            : " , len(df) - len(data1))
            print("~> Data after cleaning outliers within the data  : ", len(data1))
            
            # represent by boxplot graph formate 
            sns.boxplot(x = col_name , data = data1)
            
            new_df = pd.DataFrame(data1)
            return new_df
            
            
        else:
            print(f"column '{col_name}' does not exist in this csv file.")