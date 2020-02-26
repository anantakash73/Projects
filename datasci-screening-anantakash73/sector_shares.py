# Import pandas
import pandas as pd

# Read in html and csv file
html_data = pd.read_html('data/table.html')
eod_df = pd.read_csv('data/eod.csv')

# Get DataFrame 
html_df = html_data[0]

# We only need the symbol and sector data, so remove all other columns
html_df = html_df[['Symbol','GICS Sector']]

# Rename column names and set index to symbol column
html_df.columns = ['symbol','sector']
html_df.set_index('symbol',inplace=True)
eod_df.set_index('symbol',inplace=True)

# dict that will hold final data
industry_dict = {}

# Although not required by spec, this list contains all the companies that were not in the companies portfolio
# but had sector data
symbols_not_present = []

for i in html_df.index.values:
    try:
        industry_dict[html_df.loc[i].values[0]] = industry_dict.get(html_df.loc[i].values[0],0) + eod_df.loc[i].values[0]
        # For each symbol, look up its industry. For that industry, check if present in dict. If yes, then add the symbol's
        # share value to the value in the dict, otherwise create new key and set its value
    except:
        symbols_not_present.append(i)

# Create dataframe from industry dict
sector_df = pd.DataFrame.from_dict(industry_dict, orient='index')
sector_df.columns = ['shares_held']
sector_df.index.name = 'sector'

#Remove any duplicates if present
sector_df.drop_duplicates(inplace=True)
sector_df.to_csv('data/sector.csv')