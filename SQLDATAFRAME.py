import pandas as pd
import numpy as np


df=pd.read_csv('student-mat.csv',sep=';')

def SELECT_FROM(df):
    return df
#SELECT * FROM DF


def SELECT_FROM_LIMIT_N(df,n):
    return df.head(n)

#SELECT * FORM DF LIMIT N

def SELECT_FROM_WHERE_CONDITIONS(df,list1):
    A=df
    for l in list1:
        A=A[l]
    return A

#SELECT * FORM DF WHERE CONDITION1 AND CONDITION2 AND...
#EXAMPLE
'''
filter1=(df.sex =='M')
filter2=(df.age<=18)
filterlist=[filter1,filter2]
print(SELECT_FROM_WHERE_CONDITIONS(df,filterlist))
'''


def SELECT_FIELDS_FROM_WHERE_N(df,filterlist,fieldlist):
    A=df
    for filter in filterlist:
        A=A[filter]
    A=A[fieldlist]
    return A

#SELECT FIELD1, FIELD2, FIELD3 FORM DF WHERE CONDITION1 AND CONDITION2 AND...
#EXAMPLE
'''
filter1=(df.sex =='M')
filter2=(df.age<=18)
filterlist=[filter1,filter2]
fieldlist=['sex','age']
print(SELECT_FIELDS_FROM_WHERE_N(df,filterlist,fieldlist))
'''


def COLUMNS(df):
    return df.columns.values.tolist()
#GET THE LIST OF COLIMUNS NAMES


def SELECT_FROM_WHERE_IN_CONDITIONS(df,fieldlist,conditionlist):
    if len(fieldlist)!= len(conditionlist):
        print('You need the same amount of fields and conditions!')
        return
    for i in range(len(fieldlist)):
        filter=df[fieldlist[i]].isin(conditionlist[i])
        df=df[filter]
    return df
#SELECT * FROM DF WHERE FIELD1 IN [VALUE1, VALUE2,VALUE3] AND FIELD2 IN [VALUE1, VALUE2,VALUE3]
#EXAMPLE
'''
conditionlist=[['M'],[15,16]]
fieldlist=['sex','age']
print(SELECT_FROM_WHERE_IN_CONDITIONS(df,fieldlist,conditionlist))
'''


def SELECT_FROM_WHERE_NOT_IN_CONDITIONS(df,fieldlist,conditionlist):
    if len(fieldlist)!= len(conditionlist):
        print('You need the same amount of fields and conditions!')
        return
    for i in range(len(fieldlist)):
        List=list(np.unique(df[fieldlist[i]]))
        for x in conditionlist[i]:
            List.remove(x)
        filter= df[fieldlist[i]].isin(List)
        df=df[filter]
    return df
#SELECT * FROM DF WHERE FIELD1 NOT IN [VALUE1, VALUE2,VALUE3] AND FIELD2 NOT IN [VALUE1, VALUE2,VALUE3]
#EXAMPLE
'''
conditionlist=[['M'],[15,16]]
fieldlist=['sex','age']
print(SELECT_FROM_WHERE_NOT_IN_CONDITIONS(df,fieldlist,conditionlist))
'''



def SELECT_COUNT_FROM_GROUPBY(df,fieldlist):
    df.groupby(fieldlist,as_index=False).size().to_csv('app.csv',header=False)
    fieldlist.append('groupby')
    df=pd.read_csv('app.csv',names=fieldlist,index_col=False)
    import os
    os.remove('app.csv')
    return df
#SELECT  FIELD1, FIELD2 FROM DF GROUP BY FIELD1, FIELD2 
#EXAMPLE
'''
fieldlist=['sex','age']
print(SELECT_COUNT_FROM_GROUPBY(df,fieldlist))fieldlist=['sex','age']
print(SELECT_COUNT_FROM_GROUPBY(df,fieldlist))
'''


def SELECT_FIELDS_FROM_SORT_BY(df,fieldlist,sortfields,methodlist):
    df = df[fieldlist]
    df=df.sort_values(sortfields,ascending=methodlist)
    return df
#SELECT  FIELD1, FIELD2 FROM DF ORDER BY FIELD1 , FIELD2 DESC
#EXAMPLE
'''
fieldlist=['sex','age']
sortfields=['sex','age']
methodlist=['desc','desc']
print(SELECT_FIELDS_FROM_SORT_BY(df,fieldlist,sortfields,methodlist))
'''





def AGGREGATE_FUNCTION(df,field):
    df=df.agg({field: ['min', 'max', 'mean', 'median']})
    return df

#SELECT  FIELD1, MIN(FIELD1),MAX(FIELD1),AVG(FIELD1),MEDIAN(FIELD1) FROM DF GROUP BY FIELD1 
#EXAMPLE
'''
field='age'
print(AGGREGATE_FUNCTION(df,field))
'''



def UNION_ALL(df1,df2):
    frames=[df1,df2]
    return pd.concat(frames)

#SELECT  FIELD1, FIELD2 FROM DF WHERE CONDITION1 UNION ALL SELECT  FIELD1, FIELD2 FROM DF WHERE CONDITION2
#EXAMPLE

'''
filter1=(df.sex =='M')
filter2=(df.age<=18)
filterlist=[filter1,filter2]
df1=SELECT_FROM_WHERE_CONDITIONS(df,filterlist)
filter1=(df.sex =='F')
filter2=(df.age>18)
filterlist=[filter1,filter2]
df2=SELECT_FROM_WHERE_CONDITIONS(df,filterlist)
print(df1)
print(df2)
print(UNION_ALL(df1,df2))
'''




def SELECT_FIELDS_AGG_FUNCTION_on_FIELDS_WHERE_GROUPBY(df,filterlist,fieldlist):
    A= SELECT_FIELDS_FROM_WHERE_N(df,filterlist,fieldlist)
    if len(fieldlist)==1:
        A1=AGGREGATE_FUNCTION(A,fieldlist[0])
        return A1.T
    app=[]
    for field in fieldlist:
        app.append(AGGREGATE_FUNCTION(A,field))
    A = pd.merge(app[0], app[1], left_index=True, right_index=True)

    for i in range(2,len(app)):
        A=pd.merge(A, app[i], left_index=True, right_index=True)
    return A.T
#Creates a Dataframe with statistical infos from several fields after a where condition
#EXAMPLE
'''
filter1=(df.sex =='M')
filter2=(df.age<=18)
filterlist=[filter1,filter2]
fieldlist=['G3','G2','age','G1']
print(SELECT_FIELDS_AGG_FUNCTION_on_FIELDS_WHERE_GROUPBY(df,filterlist,fieldlist))
'''




