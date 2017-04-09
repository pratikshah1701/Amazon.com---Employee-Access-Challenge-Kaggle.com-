import numpy as np
import pandas as pd
from itertools import *
weight={}
totalWeight={}
final = pd.DataFrame(columns=['Id','Resource','Weight']);
df_test= pd.read_csv('https://raw.githubusercontent.com/pratikshah1701/Amazon.com---Employee-Access-Challenge-Kaggle.com-/master/test.csv')
#print(df_test)
df_train= pd.read_csv('https://raw.githubusercontent.com/pratikshah1701/Amazon.com---Employee-Access-Challenge-Kaggle.com-/master/train.csv')
#df_train
d={}
d1={}


All_rows_train,All_columns_train=df_train.shape

#print(" All_rows_train :- "+str(All_rows_train))
#print(" All_columns_train :- "+str(All_columns_train))


df_unique_resources = df_test['RESOURCE'].unique()
df_unique_resources.sort()
for i in range (len(df_unique_resources)):
    d[df_unique_resources[i]]= (df_train[df_train['RESOURCE'] == df_unique_resources[i]])
    d1[df_unique_resources[i]]= (df_test[df_test['RESOURCE'] == df_unique_resources[i]])


def compare(f):

    dff_train = d[f]
    dff_test = d1[f]
    rows_test,columns_test = dff_test.shape
    rows_train,columns_train = dff_train.shape
    #print(" test rows :- "+str(rows_test))
    #print(" test columns :- "+str(columns_test))
    #print(" train rows :- "+str(rows_train))
    #print(" train columns :- "+str(columns_train))

    matrix_frame_test = dff_test.as_matrix()
    matrix_frame_train = dff_train.as_matrix()

    train_row_count = 0
    train_column_count = 0
    test_row_count = 0
    test_column_count = 0

    for i in range(0, rows_train):

        each_train_row = matrix_frame_train[i]
        for x in range(0, rows_test):
            each_test_row = matrix_frame_test[x]

            count = 0
            for m in range(2, columns_train):
              if each_train_row[m] == each_test_row[m]:
                  count+=1
            #print(each_test_row[0])
            #print(" count :- "+str(count))
            #print(" action :- "+str(each_train_row[0]))
            #print(" weigth :- "+str(((count/8)*each_train_row[0])))
            weight[each_test_row[m]] = ((count/8)*each_train_row[0])
            print(((count/8)*each_train_row[0]))

    print(weight)





#print(df_unique_resources)weight
compare(38)

'''
for i in range (len(df_unique_resources)):
    compare(df_unique_resources[i])
    #totalWeight[df_unique_resources[i]]=
'''
#print(len(weigth.keys()))

'''
for keys,values in weight.items():
    print(keys)
    print(values)
    print("--")
'''
'''
for keys,values in d.items():
    print(keys)
    print(values)

df_current = pd.DataFrame()
df_current = d[38]
print(df_current)

rows_test,columns_test = df_test.shape
rows_current,columns_current = df_current.shape

matrix_frame_test = df_test.as_matrix()
matrix_frame_current = df_current.as_matrix()

test_count = 0
current_count = 0

'''
