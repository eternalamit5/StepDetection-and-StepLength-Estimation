# simple arranging of data as per sensor.csv file
# first delete start 6 lines from .txt file

import pandas as pd
df = pd.read_csv("GroundFloorData/groundFloor_KLEtofabLab_Y_axis_down-000.txt", delimiter=",")


titles= list(df.columns)
print(titles)


df.drop(df.columns[[0,11,12,13]], axis=1, inplace=True) # column 1 = index 0
#df = df.drop('PacketCounter', 1)

titles= list(df.columns)
print(titles)

df=df[titles]
print(df)

#arranging title of gyro and acc as per sensor.csv file
titles[1],titles[4]= titles[4],titles[1]
titles[2],titles[5]= titles[5],titles[2]
titles[3],titles[6]= titles[6],titles[3]
df =df[titles]
print('after title interchange')
print(df)

df.rename(columns={'SampleTimeFine': 'time', 'Acc_X': 'ax', 'Acc_Y': 'ay', 'Acc_Z': 'az', 'Gyr_X': 'gx','Gyr_Y': 'gy', 'Gyr_Z': 'gz'}, inplace=True)
print("after renaming")
print(df)

df['ax'] = (df['ax'] / 9.8)
df['ay'] = (df['ay'] / 9.8)
df['az'] = (df['az'] / 9.8)


df.to_csv("groundFloor_KLEtofabLab_Y_axis_down-000.csv", index=False,sep=',')