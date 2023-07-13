import pandas as pd
import os
import random

read = '/home/cybercamp2023/git/lab2/data/'
os.chdir(read)

file_list = [f for f in os.listdir(read) if f.endswith('.csv')]
print(file_list)

df = pd.read_csv(file_list[0])
df.columns = ['No,', 'Time', 'Protocol', 'eth.src', 'eth.dst', 'Source', 'Destination', 'Length']
print(df)

df = df[~ df['Protocol'].str.contains('HomePNA')]
df = df[~ ((df['Source'].str.contains('172')) & (df['Destination'].str.contains('172')))]
df = df[~ ((df['Source'].str.contains('192')) & (df['Destination'].str.contains('192')))]
df = df[~ ((df['Source'].str.contains('172')) & (df['Destination'].str.contains('192')))]
df = df[~ ((df['Source'].str.contains('192')) & (df['Destination'].str.contains('172')))]
df = df[~ df['Protocol'].str.contains('ARP')]
df = df[~ df['Protocol'].str.contains('XID')]
df = df[~ df['Protocol'].str.contains('MDNS')]
df = df[~ df['Protocol'].str.contains('IGMPv3')]
df = df[~ df['Protocol'].str.contains('SSDP')]
df = df[~ df['Protocol'].str.contains('ICMP')]
print(df)

df.drop(df.columns[[0, 2, 3, 4, 5, 6]], axis=1, inplace=True)
df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d  %H:%M:%S.%f')
df.index = df['Time']
df = df.drop('Time', axis=1)
df = df.Length.resample('100L').sum()
print(df)

df.to_csv('cleaned.csv')
