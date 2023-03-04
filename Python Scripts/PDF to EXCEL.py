import pandas as pd
import tabula
df = tabula.read_pdf('Bernardo Arturo Conquet Gutierrez.pdf',
                     pages = 'all',
                     guess=False,
                     pandas_options={'header':None})

data0 = df[0]
#data1 = df[1]
with pd.ExcelWriter('Bernardo Arturo Conquet Gutierrez.xlsx') as writer:  
    data0.to_excel(writer,sheet_name='Sheet1')
    #data1.to_excel(writer,sheet_name='Sheet2')