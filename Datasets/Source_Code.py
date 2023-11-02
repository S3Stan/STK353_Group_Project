# imports 
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


# parse the data files as html to datasets.
with open("Datasets/2008_honda_accord", "r") as file:
    honda_accord_2008_file = file.read()
    
with open("Datasets/2009_honda_accord", "r") as file:
    honda_accord_2009_file = file.read()
    
with open("Datasets/2009_hyundai_sonata", "r") as file:
    hyundai_sonata_2009_file = file.read()
    
with open("Datasets/2009_toyota_corolla", "r") as file:
    toyota_corolla_2009_file = file.read()




# send datasets to notebook methods
def send_honda_accord_2008_data():   
    Honda_accord_2008_data = BeautifulSoup(honda_accord_2008_file, 'html.parser') 
    return Honda_accord_2008_data # return data

def send_honda_accord_2009_data():   
    Honda_accord_2009_data = BeautifulSoup(honda_accord_2009_file, 'html.parser') 
    return Honda_accord_2009_data # return data
    
def send_hyundai_sonata_2008_data():   
    Hyundai_sonata_2009_data = BeautifulSoup(hyundai_sonata_2009_file, 'html.parser') 
    return Hyundai_sonata_2009_data # return data

def send_toyota_corolla_2009_data():   
    Toyota_corolla_2009_data = BeautifulSoup(toyota_corolla_2009_file, 'html.parser') 
    return Toyota_corolla_2009_data # return data 

    