#import pandas

import pandas as pd

# Import data into data frame, adding column names
start_df = pd.read_csv("data/start.csv", names=['symbol','shares_held'])
trades_df = pd.read_csv("data/trades.csv", names=['symbol','trade_amount'])

###
# The csv files were first operated on in a Jupyter notebook called Trades which is also part of this repo
# The final code has been included in this file

start_df.set_index('symbol',inplace=True)
trades_df.set_index('symbol',inplace=True)

# EOD dict that will store final trade volumes
end_dict = {}

# Sanity check count variable to make sure all symbols are accounted for
#count = 0

for i in start_df.index.values:
    try:
        end_dict[i] = trades_df.loc[i].sum().values[0] + start_df.loc[i].values[0] # Sum the values from trades and add to starting position
        #count +=1
    except:
        if i in trades_df.index:
            # These symbols only have one trade in the trades_df
            # Hence just need to add that trade to the starting position
            end_dict[i] = (trades_df.loc[i].sum() + start_df.loc[i]).values[0]
            #count +=1
        else:
            # These symbols were not traded, hence end of day position
            # is same as start position
            end_dict[i] = start_df.loc[i].values[0]
            #count+=1


#print(count)

# Create new dataframe to hold the eod dict
end_df = pd.DataFrame.from_dict(end_dict, orient='index')
end_df.columns = ['shares_held']
end_df.index.name = 'symbol'

#Remove any duplicates if present
end_df.drop_duplicates(inplace=True)
end_df.to_csv('data/eod.csv')
