import pyodbc

# Connect to your SQL Server database
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-U9TRIAN;DATABASE=ServiceInvoices;UID=sa;PWD=v!nay@123'
)

# Execute your SQL query
cursor = conn.cursor()
cursor.execute('SELECT [S/N] ,[Offer_L1] ,[Offer_L2]  ,[Offer_N0] ,[Offer No] ,[Revision] ,[PO Number]   ,[Po Date]    ,[Client Name]  ,[ Date]  FROM [Offers].[dbo].[22-23]')
results = cursor.fetchall()

# Close the connection
conn.close()