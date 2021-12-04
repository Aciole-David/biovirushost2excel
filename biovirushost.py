#!/home/david/miniconda2/envs/biovirushost/bin/python3

#BiovirusHost

import pandas as pd

from BioVirusHost import BioVirusHost

taxlist = open("taxID-list.txt")

lines = taxlist.readlines()

for line in lines:
    for i_result in BioVirusHost.v_tax_search([line]):
        df = pd.DataFrame(i_result)
        with pd.ExcelWriter('biovirushost.xlsx') as writer:
            df.to_excel(writer, sheet_name='Sheet1')
