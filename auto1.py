import pandas as pd 

#Table Extraction - Extract Tables from Websites
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
print(len(simpsons))
print(simpsons)
