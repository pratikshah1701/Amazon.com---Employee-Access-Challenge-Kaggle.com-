import pandas as pd


##Dataframe for Traning dataset.
df_train = pd.read_csv('https://raw.githubusercontent.com/vidushidikshit/Machine_Learning/master/train_amazon.csv')
print(df_train.head())


##Dataframe for test dataset.
df_test = pd.read_csv('https://raw.githubusercontent.com/vidushidikshit/Machine_Learning/master/test_amazon.csv')
df_test.insert(0, 'ACTION', 0)
df_test = df_test.drop('id',1)
print(df_test.head())

##Decalring Threshhold
threshold = 0.1

#df_test.insert(0, 'ACTION', 0)
#df_test = df_test.drop('id',1)
#print(df_test.head())


##Get all unique resources from the test dataset.
df_unique_resources = df_test['RESOURCE'].unique()
df_unique_resources.sort()


## Dictionary declaration.
d = {}


## Print unique resources.
print(df_unique_resources)


## Create dictionary for unique resources.
for i in range(len(df_unique_resources)):
    #print(df_unique_resources[i])
    d[df_unique_resources[i]] = df_train[df_train['RESOURCE'] == df_unique_resources[i]]

'''
##Test print dictionary for resource 0
#print(d[78766])
test_row = df_test.iloc[0]
print(test_row)
df_current = d[test_row['RESOURCE']]
print(df_current)
df_row_count = len(df_current)


Mgr_Id_Count_Pos = len(df_current[(df_current['MGR_ID'] == test_row['MGR_ID']) & (df_current['ACTION'] == 1)])/df_row_count
Role_Rollup_1_Count_Pos = len(df_current[(df_current['ROLE_ROLLUP_1'] == test_row['ROLE_ROLLUP_1']) & (df_current['ACTION'] == 1)])/df_row_count
Role_Rollup_2_Count_Pos = len(df_current[(df_current['ROLE_ROLLUP_2'] == test_row['ROLE_ROLLUP_2']) & (df_current['ACTION'] == 1)])/df_row_count
Role_Deptname_Count_Pos = len(df_current[(df_current['ROLE_DEPTNAME'] == test_row['ROLE_DEPTNAME']) & (df_current['ACTION'] == 1)])/df_row_count
Role_Title_Count_Pos = len(df_current[(df_current['ROLE_TITLE']==test_row['ROLE_TITLE']) & (df_current['ACTION'] == 1)])/df_row_count
Role_Family_Desc_Count_Pos = len(df_current[(df_current['ROLE_FAMILY'] == test_row['ROLE_FAMILY']) & (df_current['ACTION'] == 1)])/df_row_count
Role_Family_Count_Pos = len(df_current[(df_current['ROLE_FAMILY'] == test_row['ROLE_FAMILY']) & (df_current['ACTION'] == 1)])/df_row_count
Role_Code_Count_Pos = len(df_current[(df_current['ROLE_CODE'] == test_row['ROLE_CODE']) & (df_current['ACTION'] == 1)])/df_row_count

print('Manager ID Count Positive Effect :' + str(Mgr_Id_Count_Pos))
print('Role Rollup 1 Positive Effect :' + str(Role_Rollup_1_Count_Pos))
print('Role Rollup 2 Positive Effect : ' + str(Role_Rollup_2_Count_Pos))
print('Dept Name Positive Effect : ' + str(Role_Deptname_Count_Pos))
print('Role Title Positive Effect : ' + str(Role_Title_Count_Pos))
print('Role Family Desc Count Positive Effect : ' + str(Role_Family_Desc_Count_Pos))
print('Role Family Desc Positive Effect : ' + str(Role_Family_Count_Pos))
print('Role Code Positive Effect : ' + str(Role_Code_Count_Pos))

Total_Pos = (Mgr_Id_Count_Pos + Role_Rollup_1_Count_Pos + Role_Rollup_2_Count_Pos + Role_Deptname_Count_Pos + Role_Title_Count_Pos + Role_Family_Desc_Count_Pos + Role_Family_Count_Pos + Role_Code_Count_Pos)/8
print('Final Positive Value : ' + str(Total_Pos))

Mgr_Id_Count_Neg = len(df_current[(df_current['MGR_ID'] == test_row['MGR_ID']) & (df_current['ACTION'] == 0)])/df_row_count
Role_Rollup_1_Count_Neg = len(df_current[(df_current['ROLE_ROLLUP_1'] == test_row['ROLE_ROLLUP_1']) & (df_current['ACTION'] == 0)])/df_row_count
Role_Rollup_2_Count_Neg = len(df_current[(df_current['ROLE_ROLLUP_2'] == test_row['ROLE_ROLLUP_2']) & (df_current['ACTION'] == 0)])/df_row_count
Role_Deptname_Count_Neg = len(df_current[(df_current['ROLE_DEPTNAME'] == test_row['ROLE_DEPTNAME']) & (df_current['ACTION'] == 0)])/df_row_count
Role_Title_Count_Neg = len(df_current[(df_current['ROLE_TITLE']==test_row['ROLE_TITLE']) & (df_current['ACTION'] == 0)])/df_row_count
Role_Family_Desc_Count_Neg = len(df_current[(df_current['ROLE_FAMILY'] == test_row['ROLE_FAMILY']) & (df_current['ACTION'] == 0)])/df_row_count
Role_Family_Count_Neg = len(df_current[(df_current['ROLE_FAMILY'] == test_row['ROLE_FAMILY']) & (df_current['ACTION'] == 0)])/df_row_count
Role_Code_Count_Neg = len(df_current[(df_current['ROLE_CODE'] == test_row['ROLE_CODE']) & (df_current['ACTION'] == 0)])/df_row_count

print('Manager ID Count Negative Effect :' + str(Mgr_Id_Count_Neg))
print('Role Rollup 1 Negative Effect :' + str(Role_Rollup_1_Count_Neg))
print('Role Rollup 2 Negative Effect : ' + str(Role_Rollup_2_Count_Neg))
print('Dept Name Negative Effect : ' + str(Role_Deptname_Count_Neg))
print('Role Title Negative Effect : ' + str(Role_Title_Count_Neg))
print('Role Family Desc Count Negative Effect : ' + str(Role_Family_Desc_Count_Neg))
print('Role Family Desc Negative Effect : ' + str(Role_Family_Count_Neg))
print('Role Code Negative Effect : ' + str(Role_Code_Count_Neg))

Total_Neg = (Mgr_Id_Count_Neg + Role_Rollup_1_Count_Neg + Role_Rollup_2_Count_Neg + Role_Deptname_Count_Neg + Role_Title_Count_Neg + Role_Family_Desc_Count_Neg + Role_Family_Count_Neg + Role_Code_Count_Neg)/8
print('Final Negative Value : ' + str(Total_Neg))

Final_Value = Total_Pos + Total_Neg
print(Final_Value)

if(Final_Value > threshold):
    test_row['ACTION'] = 1

print(test_row)

print(df_test.head())
'''


##Main calculation
for index, row in  df_test.iterrows():
    #print(row)
    df_current = d[row['RESOURCE']]
    #print(df_current)
    df_row_count = len(df_current)

    #Calculate all the positive results.
    Mgr_Id_Count_Pos = len(df_current[(df_current['MGR_ID'] == row['MGR_ID']) & (df_current['ACTION'] == 1)])/df_row_count
    Role_Rollup_1_Count_Pos = len(df_current[(df_current['ROLE_ROLLUP_1'] == row['ROLE_ROLLUP_1']) & (df_current['ACTION'] == 1)])/df_row_count
    Role_Rollup_2_Count_Pos = len(df_current[(df_current['ROLE_ROLLUP_2'] == row['ROLE_ROLLUP_2']) & (df_current['ACTION'] == 1)])/df_row_count
    Role_Deptname_Count_Pos = len(df_current[(df_current['ROLE_DEPTNAME'] == row['ROLE_DEPTNAME']) & (df_current['ACTION'] == 1)])/df_row_count
    Role_Title_Count_Pos = len(df_current[(df_current['ROLE_TITLE']==row['ROLE_TITLE']) & (df_current['ACTION'] == 1)])/df_row_count
    Role_Family_Desc_Count_Pos = len(df_current[(df_current['ROLE_FAMILY'] == row['ROLE_FAMILY']) & (df_current['ACTION'] == 1)])/df_row_count
    Role_Family_Count_Pos = len(df_current[(df_current['ROLE_FAMILY'] == row['ROLE_FAMILY']) & (df_current['ACTION'] == 1)])/df_row_count
    Role_Code_Count_Pos = len(df_current[(df_current['ROLE_CODE'] == row['ROLE_CODE']) & (df_current['ACTION'] == 1)])/df_row_count

    '''
    print('Manager ID Count Positive Effect :' + str(Mgr_Id_Count_Pos))
    print('Role Rollup 1 Positive Effect :' + str(Role_Rollup_1_Count_Pos))
    print('Role Rollup 2 Positive Effect : ' + str(Role_Rollup_2_Count_Pos))
    print('Dept Name Positive Effect : ' + str(Role_Deptname_Count_Pos))
    print('Role Title Positive Effect : ' + str(Role_Title_Count_Pos))
    print('Role Family Desc Count Positive Effect : ' + str(Role_Family_Desc_Count_Pos))
    print('Role Family Desc Positive Effect : ' + str(Role_Family_Count_Pos))
    print('Role Code Positive Effect : ' + str(Role_Code_Count_Pos))
    '''

    Total_Pos = (Mgr_Id_Count_Pos + Role_Rollup_1_Count_Pos + Role_Rollup_2_Count_Pos + Role_Deptname_Count_Pos + Role_Title_Count_Pos + Role_Family_Desc_Count_Pos + Role_Family_Count_Pos + Role_Code_Count_Pos)/8
    #print('Final Positive Value : ' + str(Total_Pos))

    ##Calculate all the negative results.
    Mgr_Id_Count_Neg = len(df_current[(df_current['MGR_ID'] == row['MGR_ID']) & (df_current['ACTION'] == 0)])/df_row_count
    Role_Rollup_1_Count_Neg = len(df_current[(df_current['ROLE_ROLLUP_1'] == row['ROLE_ROLLUP_1']) & (df_current['ACTION'] == 0)])/df_row_count
    Role_Rollup_2_Count_Neg = len(df_current[(df_current['ROLE_ROLLUP_2'] == row['ROLE_ROLLUP_2']) & (df_current['ACTION'] == 0)])/df_row_count
    Role_Deptname_Count_Neg = len(df_current[(df_current['ROLE_DEPTNAME'] == row['ROLE_DEPTNAME']) & (df_current['ACTION'] == 0)])/df_row_count
    Role_Title_Count_Neg = len(df_current[(df_current['ROLE_TITLE']==row['ROLE_TITLE']) & (df_current['ACTION'] == 0)])/df_row_count
    Role_Family_Desc_Count_Neg = len(df_current[(df_current['ROLE_FAMILY'] == row['ROLE_FAMILY']) & (df_current['ACTION'] == 0)])/df_row_count
    Role_Family_Count_Neg = len(df_current[(df_current['ROLE_FAMILY'] == row['ROLE_FAMILY']) & (df_current['ACTION'] == 0)])/df_row_count
    Role_Code_Count_Neg = len(df_current[(df_current['ROLE_CODE'] == row['ROLE_CODE']) & (df_current['ACTION'] == 0)])/df_row_count

    '''
    print('Manager ID Count Negative Effect :' + str(Mgr_Id_Count_Neg))
    print('Role Rollup 1 Negative Effect :' + str(Role_Rollup_1_Count_Neg))
    print('Role Rollup 2 Negative Effect : ' + str(Role_Rollup_2_Count_Neg))
    print('Dept Name Negative Effect : ' + str(Role_Deptname_Count_Neg))
    print('Role Title Negative Effect : ' + str(Role_Title_Count_Neg))
    print('Role Family Desc Count Negative Effect : ' + str(Role_Family_Desc_Count_Neg))
    print('Role Family Desc Negative Effect : ' + str(Role_Family_Count_Neg))
    print('Role Code Negative Effect : ' + str(Role_Code_Count_Neg))
    '''

    Total_Neg = (Mgr_Id_Count_Neg + Role_Rollup_1_Count_Neg + Role_Rollup_2_Count_Neg + Role_Deptname_Count_Neg + Role_Title_Count_Neg + Role_Family_Desc_Count_Neg + Role_Family_Count_Neg + Role_Code_Count_Neg)/8
    #print('Final Negative Value : ' + str(Total_Neg))

    Final_Value = Total_Pos - Total_Neg
    print(str(index)+' : '+str(Final_Value))

    ##Set Action
    if(Final_Value > threshold):
        row['ACTION'] = 1

    #print(row)

    #print(df_test.head())


df_test.to_csv(str(threshold)+'.csv')
