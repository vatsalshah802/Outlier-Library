# import seaborn library
import pandas as pd
import seaborn as sns

class detection:
    
    @staticmethod

    def outlier_detect(df,col_name):
        
        # check your column is exists or not in your dataframe
        
        if col_name in df.columns:
            
            #using outlier remove by manually method
            
            column_data = df[col_name]
            
            
            Q1 = df[col_name].quantile(25/100)
            Q2 = df[col_name].quantile(50/100)
            Q3 = df[col_name].quantile(75/100)
            
            # counting Initial Quartile Range
            IQR = Q3-Q1
            
            lower_limit = Q1 - (1.5*IQR)
            upper_limit = Q3 + (1.5*IQR)
            
            a  = [i for i in df[col_name] if lower_limit > i or upper_limit < i]
            
            # here now check above process outlier in existing this perticuler column in dataset ?
            
            if a :
                print()
                print("~> Outliers : ", a)
                print()
                print("~> Count of Outliers : ", len(a))
                print()
                print("~> Percentage of Outlier in your selectd column : " ,round((len(a)/len(df[col_name]))*100,2), "%")
                
                 # represent by boxplot graph formate 
                sns.boxplot(x = col_name, data = df)
                
                
            else:
                print("Outlier are not found for your selected column in this dataset.")
                
        else:
            print(f"column {col_name} is does not exist in the csv file.")

            