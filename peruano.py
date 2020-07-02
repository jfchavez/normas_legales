# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:42:31 2018
Script to download Normas Legales, daily from 2000 to NOW
Needs script from Stata to set dates and links
@author: Jorge F. Chavez
"""

import urllib2
import os
import csv

os.chdir("D:\\Dropbox\\Data\Peru\\Politica\\peruano")
#file("savinghtml_example.html", "w").write(urllib2.urlopen("http://www.aduanet.gob.pe/ol-ad-itconsultadua/RPSGDui?ndui=1180410007745").read())

def download_file(file_name, download_url):
    response = urllib2.urlopen(download_url)
    file = open(os.path.join('normas',file_name + ".pdf"), 'wb')
    file.write(response.read())
    file.close()
    print(file_name)


inputfile = 'peruanolinks.csv'
with open(os.path.join('inputs', inputfile), 'rb') as f:
    reader = csv.reader(f)
    ids = list(reader)

pos = 0    
for id in ids[pos:]:
    fileid = id[1]
    link = id[0]
    try:
        download_file(fileid,link)                     
    except:
        print 'There was an error in ' + link



