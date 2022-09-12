from bs4 import BeautifulSoup
import requests
#location of the data
result_file = "law_order_svu_passwords_2.txt"

#open file, w mode clears out file
f = open(result_file, 'w')

#Wikipedia URL to pull the HTML data from 
url="https://en.wikipedia.org/wiki/List_of_Law_%26_Order:_Special_Victims_Unit_episodes_(seasons_1%E2%80%9319)"
#GET the data/html
html_content = requests.get(url).text
#into soup
soup = BeautifulSoup(html_content, "lxml")
#get the tables. Using class wikitable plainrowheaders wikiepisodetable to pull the actual information that I need.
gdp_table = soup.find("table", attrs={"class":"wikitable plainrowheaders wikiepisodetable"})
#using the selector td + class:summary to pull all the episodes from the tables as rows
rows = soup.find_all("td", attrs={"class":"summary"})
#looping all the selected rows
for row in rows:	
	#a little clean up. removing spaces, single quotes and semicolons.
	clean_row = row.get_text()
	clean_row = clean_row.replace(" ", "").replace("'", "").replace(":", "").replace('"', "").lower()				
	#loop from 1-99 	
	for x in range(1, 100):		
		#write the result to the password file
		f.write(clean_row + str(x).zfill(2) + '\n') #zfill to format leading zeroes
f.close()
print("done!")
