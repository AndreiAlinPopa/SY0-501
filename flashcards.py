from tkinter import *
import pandas as pd
import os
import random
import time

print("Initializaing....")
time.sleep(0.5)

def chapter_select(chapter):
    """
    chapter: takes int 1-10
    returns: str directory of desired file
    """
    chapter -= 1
    chapterNames = (
     "Chapter 1 - Risk Management.xlsx", 
     "Chapter 2 - Cryptography.xlsx",
     "Chapter 3 - Identity and Access Management.xlsx",
     "Chapter 4 -",
     "Chapter 5 - Securing Individual Systems.xlsx",
     "Chapter 6 - The Basic LAN")
    
    directory = os.getcwd()

    return directory + "\\" + chapterNames[chapter]

def zip_chapter(detail, notes):
    """
    detail: list from column detail
    notes: list from column notes
    returns: dictionary, detail is keys, notes is values
    """
    dictionary = dict(zip(detail, notes))
    return dictionary

def read_chapter(selectedChapter):
    """
    selectedChapter: int of chapter
    returns: 2 lists
    """
    file = chapter_select(selectedChapter)
    readFile = pd.read_excel(file)
    
    detail = readFile.loc[:, 'Detail']
    notes = readFile.loc[:, 'Notes']
    
    detail = detail.tolist()
    notes = notes.tolist()
    
    dictionary = zip_chapter(detail, notes)
    
    return dictionary

def query_dict(dictionary, topics, entry):
    """
    entry: takes rng int number to pick entry
    """
    print(topics[entry])
    time.sleep(2)
    print(dictionary[topics[entry]])




dictionary = read_chapter(int(input("Please enter a chapter number: ")))
termsInDict = len(dictionary.keys())
print("There are " + str(termsInDict) + " entries in this chapter.")
time.sleep(2)

topics = list(dictionary.keys())
randomInt = random.randint(0, termsInDict)

query_dict(dictionary, topics, randomInt)
    













