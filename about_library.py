def info():
    print("..........Welcome Outlier of Python Package..........")
    print()
    print("@ Module-1)")
    print("""
--> first check in your column data in exists outlier or not...
--> if yes then detect outlier in column data.
--> Ex :- import outlier_process
          from outlier_process import detection_process
          detection_process.detection.outlier_detect(df,column_name)""")
    print()
    print("@ Module-2)")
    print("""
--> Now we remove outlier data in your column data using by trimming method. 
--> Ex :- import outlier_process
          from outlier_process import clean_by_trimming
          new_variable = clean_by_trimming.clean1.trim_process(df,column_name)""")
    print() 
    print("@ Module-3)")
    print("""
--> Also we can do this change the outlier value to 
upper limit or lower limit using by capping method 
--> Ex :- import outlier_process
          from outlier_process import clean_by_capping
          new_variable = clean_by_capping.clean2.cap_process(df,column_name)""")
    print()
    print("@ Recommendations : ")
    print("""
--> In Statistic, the choice between trimming and capping methods depends on 
various factors such as the nature of the data and the specific analysis being conducted. 
--> just if founded outlier between 0 % to 1% lie so you can use trimming method 
& if founded outlier above 1% lie so you can use capping method.""")
    