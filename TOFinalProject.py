#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:16:37 2019

@author: jessicajakoby
"""

import sqlite3
import csv
import json



DB = "/Users/jessicajakoby/Library/Mobile Documents/com~apple~CloudDocs/WN_2019/TO412/TO412FinalProject.db"

conn = sqlite3.connect(DB)

curs = conn.cursor()

sqlCMD = """SELECT * FROM 'crime'"""

sqlCMD = """SELECT c.neighborhoodId, c.chargeCode, c.description, count(*) 
from 'crime' c inner join 'charge' h on c.chargecode=h.chargeCode 
where c.neighborhoodId is not null 
group by c.neighborhoodId, h.chargeCode 
ORDER BY c.
neighborhoodId, count(*) DESC"""

#curs.execute(sqlCMD)
#for row in curs:
#    print(row)
    

#%%
# Find all zipcodes within certain radius of provided zipcode
import requests
 

def proximityZips(zipOrigin, distanceMI):
    zip_code = zipOrigin
    distance = distanceMI
    zipURL = "https://www.zipcodeapi.com/rest/31TmRD79h6DmeHunEpX5jQ0xmFL9KZNnI6SNdsuKl6ymzv3tbjQwH8h7rtc4gvms/radius.json/" + zip_code + "/" + distance + "/mile"
    zipsJson = requests.get(zipURL).json()
    zips = zipsJson["zip_codes"]
    zipsL = []
    for z in zips:
        zipsL.append(z["zip_code"])
    return zipsL


zips48201 = proximityZips("48201", "5")
strzips48201 = "', '".join(str(z) for z in zips48201)
strzips48201 = """('""" + strzips48201 + """')"""
#print(strzips48201)


#%%

#create a table with all the crimes within zipcode list on days of a game


def sqlCMD_w_zips(sql, zip_string):
    sqlCMD = sql + zip_string
    print(sqlCMD)
    return sqlCMD



sqlCMD_c_t = """SELECT c.chargeCode, c.incidentTime, c.zip
    FROM 'crime' c INNER JOIN 'tigers' t ON substr(c.incidentTime, 1, 10)  = substr(t.game_time, 1, 10)
    WHERE c.zip IN """

sqlCODE = sqlCMD_w_zips(sqlCMD_c_t, strzips48201)

curs.execute(sqlCODE)
for row in curs:
   print(row)















