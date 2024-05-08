from lib.diary_entry import *

"""
Given a title and some contents
format() method returns a formatted entry:
""My Title: These are the contents"
"""

def test_formatted_entry():
    diary = DiaryEntry("Monday 5th Feb: ", "Today was a productive day")
    result = diary.format()
    assert result == "Monday 5th Feb: " "Today was a productive day"
    
"""
count_words() method returns a integer 
with the number of words in the contents
"""

def test_length_of_words_in_entry():
    diary = DiaryEntry("Monday 5th Feb: ", "Today was a productive day")
    result = diary.count_words()
    assert result == 26

"""
Given a wpm of 2 and 3 words
reading_time() returns a integer for reading time

"""
def test_reading_time_of_two_wpm_3_words():
    diary = DiaryEntry("Todays Date: ", "one, two, three")
    result = diary.reading_time(wpm=2)
    assert result == 2
    
"""
Given a wpm of 2 and 4 words
reading_time() returns a integer for reading time

"""    

def test_reading_time_of_two_wpm_4_words():
    diary = DiaryEntry("Todays Date: ", "one, two, three")
    result = diary.reading_time(wpm=2)
    assert result == 2
    
"""
Given a wpm of 50 and 100 words
reading_time() returns a integer for reading time

"""    

def test_reading_time_of_two_wpm_4_words():
    diary = DiaryEntry("Todays Date: ", 
    """one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five
    one, two, three four five""")

    result = diary.reading_time(wpm=50)
    assert result == 2
    
"""
Given 10 words
With a wpm of 2
Reading time 2 minutes
reading_chunk() returns the first 4 words
"""

def test_reading_time_of_chunk_with_2_minutes():
    diary = DiaryEntry("Todays Date: ", "one two three four five six seven eight nine ten")
    result = diary.reading_chunk(wpm=2, minutes=2)
    assert result == "one two three four"


def test_reading_time_of_chunk_with_1_minute():
    diary = DiaryEntry("Todays Date: ", "one two three four five six seven eight nine ten")
    result = diary.reading_chunk(wpm=2, minutes=1)
    assert result == "one two"