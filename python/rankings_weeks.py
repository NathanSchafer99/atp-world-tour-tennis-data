import csv
import array
from functions import html_parse_tree, xpath_parse, regex_strip_array, array2csv

weeks_url = "http://www.atpworldtour.com/en/rankings/singles"
weeks_tree = html_parse_tree(weeks_url)
weeks_xpath = "//ul[@data-value = 'rankDate']/li/@data-value"
weeks_parsed = xpath_parse(weeks_tree, weeks_xpath)
weeks_cleaned = regex_strip_array(weeks_parsed)

f = open('weeks.csv','w')
for row in weeks_cleaned:
    f.write(row + "\n") #Give your csv text here.
## Python will convert \n to os.linesep
f.close()
