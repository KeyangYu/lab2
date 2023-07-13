import os
import pandas as pd

# Change directory to working directory and delete existing csv files
os.chdir('/home/cybercamp2023/git/lab2/data/')
os.system('find . -name "*.csv" -type f -delete')
print('Current working directory is: ', os.getcwd(), '\n')

# list all the pcap/pcapng files within this directory
file_list = os.listdir('/home/cybercamp2023/git/lab2/data/')
print('Current pcap files are: ', file_list)

# Run tshark scripts to convert pcap to csv
print('Now converting pcap files to csv')
for files in file_list:
	os.system('tshark -r '
		  + files + ' -T fields -e frame.number -e_ws.col.Time -e_ws.col.Protocol -e eth.src '
		            '-e eth.dst -e ip.src -e ip.dst -e frame.len '
		            '-E occurrence=f -E header=y -E separator=, >'
		  + ' ' + files + '.csv')
print('Converting finished.')

