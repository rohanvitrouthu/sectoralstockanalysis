import pandas as pd
import glob
import os

# Set the directory containing the CSV files
os.chdir('/home/rohan/Downloads/MPS DS Course Materials/DATA 606/sectoralstockanalysis/Dataset/Merged Data/Modified')

# List all CSV files in the directory
all_filenames = [i for i in glob.glob('*.csv')]

# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

# Export to a new CSV file
combined_csv.to_csv('All_sectors.csv', index=False, encoding='utf-8-sig')
