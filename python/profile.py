# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import csv
import time
#import requests
#import re
from functions import html_parse_tree, xpath_parse, regex_strip_array, read_csv, array2csv

def checkIfEmptyReturnFirst(inList):
    if birthplace_cleaned:
        return birthplace_cleaned[0]
    else:
        return 'empty'

new_rows = []
profiles = [['player_id', 'player_slug', 'first_name', 'last_name', 'rank', 'player_url', 'profile_picture', 'flag_code', 'residence', 'birthplace', 'birthdate', 'birth_year', 'birth_month', 'birth_day', 'turned_pro', 'weight_lbs', 'weight_kg', 'height_ft', 'height_inches', 'height_cm', 'handedness', 'backhand', 'coach']]
#profile_pictures = []

start = time.time()
with open('rankings_0_2019-01-14.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    row1 = next(readCSV)
    new_row = row1
    new_row.append('profile_picture')
    new_rows.append(new_row)
    for row in readCSV:
        print(row[5])
        
        new_row = row
        profile_url = "http://www.atptour.com" + row[11]
        profile_tree = html_parse_tree(profile_url)
        
        player_thumbnaul_xpath = "//meta[@name='thumbnail']/@content"
        player_thumbnail_parsed = xpath_parse(profile_tree, player_thumbnaul_xpath)
        player_thumbnail_cleaned = regex_strip_array(player_thumbnail_parsed)
        
        new_row.append(player_thumbnail_cleaned[0])
        #profile_pictures.append(player_thumbnail_cleaned[0])
        new_rows.append(new_row)
        
        #Get profile data
        player_id = row[15]
        
        player_slug = row[12]
        
        
        first_name_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div/div/div/div[@class='first-name']/text()"
        first_name_parsed = xpath_parse(profile_tree, first_name_xpath)
        first_name_cleaned = regex_strip_array(first_name_parsed)
        
        last_name_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div/div/div/div[@class='last-name']/text()"
        last_name_parsed = xpath_parse(profile_tree, last_name_xpath)
        last_name_cleaned = regex_strip_array(last_name_parsed)
        
        rank = row[5]
        
        player_url = row[11]
        
        profile_picture = row[16]
        
        flag_code = row[14]
        
        residence_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[2]/td[2]/div/div[@class='table-value']/text()"
        residence_parsed = xpath_parse(profile_tree, residence_xpath)
        residence_cleaned = regex_strip_array(residence_parsed)
        
        birthplace_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[2]/td[1]/div/div[@class='table-value']/text()"
        birthplace_parsed = xpath_parse(profile_tree, birthplace_xpath)
        birthplace_cleaned = regex_strip_array(birthplace_parsed)
        
        profiles.append([player_id, player_slug, checkIfEmptyReturnFirst(first_name_cleaned), checkIfEmptyReturnFirst(last_name_cleaned), rank, player_url, profile_picture, flag_code, checkIfEmptyReturnFirst(residence_cleaned), checkIfEmptyReturnFirst(birthplace_cleaned), '', '', '', '', '', '', '', '', '', '', '', '', ''])
        
array2csv(new_rows, 'rankings_0_2019-01-14')

array2csv(profiles, 'profiles')

end = time.time()
print(end - start)