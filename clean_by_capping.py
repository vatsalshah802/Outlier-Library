# import pandas & seaborn library
import pandas  as pd
import seaborn as sns

class clean2:
    
    @staticmethod

    def cap_process(df,col_name):
        
         # check your column is exists or not in your dataframe
            
        if col_name in df.columns:
            
             #using outlier remove by manually method
            column_data = df[col_name]
            
            Q1 = df[col_name].quantile(25/100)
            Q2 = df[col_name].quantile(50/100)
            Q3 = df[col_name].quantile(75/100)
            
            # counting Initial Quartile Range
            IQR = Q3-Q1
            
            l = Q1 - (1.5*IQR)
            u = Q3 + (1.5*IQR)
            
            # here use .copy() function bcoz whatever I change does not change in my existing data
            data2 = df.copy()
            
            data2.loc[data2[col_name]>= u, col_name] = u 
            data2.loc[data2[col_name]<= l, col_name] = l
        
            
            print("Data Before Outlier : ", len(df))
            print("Data After Outlier : ", len(data2))
            print("Outlier = ", len(df)-len(data2))
            print()
            print("founded outliers are existing upper boundry and lower boundry")
            
             # represent by boxplot graph formate 
            sns.boxplot(x = col_name, data = data2)
            
            new_df = pd.DataFrame(data2)
            return new_df
        
        else:
            print(f"column '{col_name}' does not exist in the csv file.")
            