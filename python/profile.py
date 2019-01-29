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
from functions import html_parse_tree, xpath_parse, regex_strip_array, read_csv, array2csv, array2csv8utf


def checkIfEmptyReturnFirst(inList):
    if inList:
        return inList[0]
    else:
        return ''

def conYear(inList):
    if inList:
        dateString = inList[0]
        yearString = dateString[1:5]
        return yearString
    else:
        return ''


def conMonth(inList):
    if inList:
        dateString = inList[0]
        monthString = dateString[6:8]
        return monthString
    else:
        return ''


def conDay(inList):
    if inList:
        dateString = inList[0]
        dayString = dateString[9:11]
        return dayString
    else:
        return ''


new_rows = []
profiles = [['player_id', 'player_slug', 'first_name', 'last_name', 'rank', 'player_url', 'profile_picture', 'flag_code', 'residence', 'birthplace', 'birthdate', 'birth_year', 'birth_month', 'birth_day', 'turned_pro', 'weight_lbs', 'weight_kg', 'height_ft', 'height_inches', 'height_cm', 'handedness', 'backhand', 'coach', 'career_high', 'career_high_date', 'prize_money_year', 'prize_money', 'titles_year', 'titles', 'win_loss_year', 'win_loss']]

start = time.time()
with open('rankings_0_2019-01-28.csv') as csvfile:
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
        new_rows.append(new_row)
        
        # Get profile data
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

        birthdate_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[1]/td[1]/div/div[2]/span/span/text()"
        birthdate_parsed = xpath_parse(profile_tree, birthdate_xpath)
        birthdate_cleaned = regex_strip_array(birthdate_parsed)

        birth_year = conYear(birthdate_cleaned)
        birth_month = conMonth(birthdate_cleaned)
        birth_day = conDay(birthdate_cleaned)

        turned_pro_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[1]/td[2]/div/div[2]/text()"
        turned_pro_parsed = xpath_parse(profile_tree, turned_pro_xpath)
        turned_pro_cleaned = regex_strip_array(turned_pro_parsed)

        weight_lbs_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[1]/td[3]/div/div[2]/span/span[1]/text()"
        weight_lbs_parsed = xpath_parse(profile_tree, weight_lbs_xpath)
        weight_lbs_cleaned = regex_strip_array(weight_lbs_parsed)

        weight_kg_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[1]/td[3]/div/div[2]/span[2]/text()"
        weight_kg_parsed = xpath_parse(profile_tree, weight_kg_xpath)
        weight_kg_cleaned = regex_strip_array(weight_kg_parsed)
        weight_kg_cleaned_extracted = ''
        if checkIfEmptyReturnFirst(weight_kg_cleaned) != '':
            weight_kg_cleaned_extracted = checkIfEmptyReturnFirst(weight_kg_cleaned)[1:-3]

        height_ft_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[1]/td[4]/div/div[2]/span/span/text()"
        height_ft_parsed = xpath_parse(profile_tree, height_ft_xpath)
        height_ft_cleaned = regex_strip_array(height_ft_parsed)
        height_ft_cleaned_extracted, height_inches = '', ''
        if checkIfEmptyReturnFirst(height_ft_cleaned) != '':
            height_ft_cleaned_extracted, height_inches = checkIfEmptyReturnFirst(height_ft_cleaned).split("'")

        height_cm_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[1]/td[4]/div/div[2]/span[2]/text()"
        height_cm_parsed = xpath_parse(profile_tree, height_cm_xpath)
        height_cm_cleaned = regex_strip_array(height_cm_parsed)
        height_cm_cleaned_extracted = ''
        if checkIfEmptyReturnFirst(height_cm_cleaned) != '':
            height_cm_cleaned_extracted = checkIfEmptyReturnFirst(height_cm_cleaned)[1:-3]

        handedness_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[2]/td[3]/div/div[2]/text()"
        handedness_parsed = xpath_parse(profile_tree, handedness_xpath)
        handedness_cleaned = regex_strip_array(handedness_parsed)
        handedness_cleaned_extracted, backhand = '', ''
        if checkIfEmptyReturnFirst(handedness_cleaned) != '':
            handedness_cleaned_extracted, backhand = checkIfEmptyReturnFirst(handedness_cleaned).split(',')

        coach_xpath = "//div[@id='playerProfileHero']/div[@class='player-profile-hero-overflow']/div[@class='player-profile-hero-table']/div/table/tr[2]/td[4]/div/div[2]/text()"
        coach_parsed = xpath_parse(profile_tree, coach_xpath)
        coach_cleaned = regex_strip_array(coach_parsed)

        career_high_xpath = "//div[@id='currentTabContent']/div[@class='overview-stats-table-wrapper']/table/tbody/tr[2]/td[2]/div[1]/text()"
        career_high_parsed = xpath_parse(profile_tree, career_high_xpath)
        career_high_cleaned = regex_strip_array(career_high_parsed)

        career_high_date_xpath = "//div[@id='currentTabContent']/div[@class='overview-stats-table-wrapper']/table/tbody/tr[2]/td[2]/div[2]/text()"
        career_high_date_parsed = xpath_parse(profile_tree, career_high_date_xpath)
        career_high_date_cleaned = regex_strip_array(career_high_date_parsed)
        career_high_date_cleaned_extracted = ''
        if checkIfEmptyReturnFirst(career_high_date_cleaned) != '':
            career_high_date_cleaned_extracted = checkIfEmptyReturnFirst(career_high_date_cleaned)[-8:]

        prize_money_year_xpath = "//div[@id='currentTabContent']/div[@class='overview-stats-table-wrapper']/table/tbody/tr[1]/td[6]/div[1]/text()"
        prize_money_year_parsed = xpath_parse(profile_tree, prize_money_year_xpath)
        prize_money_year_cleaned = regex_strip_array(prize_money_year_parsed)

        prize_money_xpath = "//div[@id='currentTabContent']/div[@class='overview-stats-table-wrapper']/table/tbody/tr[2]/td[5]/div[1]/text()"
        prize_money_parsed = xpath_parse(profile_tree, prize_money_xpath)
        prize_money_cleaned = regex_strip_array(prize_money_parsed)

        titles_year_xpath = "//div[@id='currentTabContent']/div[@class='overview-stats-table-wrapper']/table/tbody/tr[1]/td[5]/div[1]/text()"
        titles_year_parsed = xpath_parse(profile_tree, titles_year_xpath)
        titles_year_cleaned = regex_strip_array(titles_year_parsed)

        titles_xpath = "//div[@id='currentTabContent']/div[@class='overview-stats-table-wrapper']/table/tbody/tr[2]/td[4]/div[1]/text()"
        titles_parsed = xpath_parse(profile_tree, titles_xpath)
        titles_cleaned = regex_strip_array(titles_parsed)

        win_loss_year_xpath = "//div[@id='currentTabContent']/div[@class='overview-stats-table-wrapper']/table/tbody/tr[1]/td[4]/div[1]/text()"
        win_loss_year_parsed = xpath_parse(profile_tree, win_loss_year_xpath)
        win_loss_year_cleaned = regex_strip_array(win_loss_year_parsed)

        win_loss_xpath = "//div[@id='currentTabContent']/div[@class='overview-stats-table-wrapper']/table/tbody/tr[2]/td[3]/div[1]/text()"
        win_loss_parsed = xpath_parse(profile_tree, win_loss_xpath)
        win_loss_cleaned = regex_strip_array(win_loss_parsed)

        profiles.append([player_id, player_slug, checkIfEmptyReturnFirst(first_name_cleaned), checkIfEmptyReturnFirst(last_name_cleaned), rank, player_url, profile_picture, flag_code, checkIfEmptyReturnFirst(residence_cleaned), checkIfEmptyReturnFirst(birthplace_cleaned), checkIfEmptyReturnFirst(birthdate_cleaned), birth_year, birth_month, birth_day, checkIfEmptyReturnFirst(turned_pro_cleaned), checkIfEmptyReturnFirst(weight_lbs_cleaned), weight_kg_cleaned_extracted, height_ft_cleaned_extracted, height_inches, height_cm_cleaned_extracted, handedness_cleaned_extracted, backhand, checkIfEmptyReturnFirst(coach_cleaned), checkIfEmptyReturnFirst(career_high_cleaned), career_high_date_cleaned_extracted, checkIfEmptyReturnFirst(prize_money_year_cleaned), checkIfEmptyReturnFirst(prize_money_cleaned), checkIfEmptyReturnFirst(titles_year_cleaned), checkIfEmptyReturnFirst(titles_cleaned), checkIfEmptyReturnFirst(win_loss_year_cleaned), checkIfEmptyReturnFirst(win_loss_cleaned)])
        
array2csv(new_rows, 'rankings_0_2019-01-14')

# array2csv(profiles, 'profiles')
array2csv8utf(profiles, 'profiles')

end = time.time()
print(end - start)
