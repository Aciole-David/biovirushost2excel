#!/home/david/miniconda2/envs/biovirushost/bin/python3

#BiovirusHost

#we need pandas
import pandas as pd

#pd.set_option('display.max_colwidth', None)

#import BioVirusHost as bvh
# all credits to https://github.com/AliYoussef96/BioVirusHost
from BioVirusHost import BioVirusHost

df_list = []

#read taxID list file
taxlist = open("taxID-list.txt")

#store each taxID lines
lines = taxlist.readlines()

#pass lines to BioVirusHost.v_tax_search parameter
for line in lines:
    for i_result in BioVirusHost.v_tax_search([line]):
        df_list.append(pd.DataFrame(i_result))
        #print(df)

df = pd.concat(df_list)

#Write dataframe in a pretty Excel worksheet
writer = pd.ExcelWriter('biovirushost.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
workbook=writer.book
worksheet = writer.sheets['Sheet1']
    
format = workbook.add_format({'text_wrap': True, 'center_across': True, 'align': 'center','valign': 'vcenter'}) #wrap text

# Setting the format but not setting the column width.
worksheet.set_column('A:E', 30, format)
writer.save()
            
            
            
            
            
            
#I like to skip bottom lines :)            
