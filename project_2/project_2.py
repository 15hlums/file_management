import string
from collections import Counter
import pygal

# splitting chapters
def start_end(author, text, file, start_line, end_line):
    '''

    :param start_line: this is the starting line of the chapter
    :param end_line: this is the ending line of the chapter
    :return: this returns the start line and the end line of the chapter
    '''
    with open(''+author+'/'+text+'/'+file+'.txt', 'r', encoding='UTF-8') as f: # this is changed depending on what novel needs spliting
        lines = f.readlines()
        return lines[start_line - 1:end_line - 1]

def line_numbers_sherlock(chapter_num): # the adventures of sherlock holmes
    '''

    :param chapter_num: this is the number of the chapter
    :return: this returns the start and end lines of a chapter and the chapter number for the adventures of sherlock holmes
    '''
    with open('arthur.conan.doyle/sherlock_holmes/adventures_sherlock_holmes.txt', 'r', encoding='UTF-8') as f:
        line_num = 0
        chapter_lines = []
        for line in f:
            line_num += 1 # counts line number
            if 57 < line_num < 11946: # this is to cut the boilerplates off the novel
                if len(list(line)) > 1:
                    if (line.isupper() and len(line) > 5 and line.strip()[-1] != '”' and line.strip()[-1] != '’') or 'EBook' in line:
                        chapter_lines.append(line_num) # append the number to the chapter lines
        line_info = (chapter_lines[chapter_num - 1:chapter_num + 1], chapter_num)
        return line_info

def line_numbers_hounds(chapter_num): # the hounds of baskervilles
    '''

    :param chapter_num: this is the number of the chapter
    :return: this returns the start and end lines of a chapter and the chapter number for the hounds of baskervilles
    '''
    with open('arthur.conan.doyle/hound_baskervilles/the_hound_of_baskervilles.txt', 'r', encoding='UTF-8') as f:
        line_num = 0
        chapter_lines = []
        for line in f:
            line_num += 1
            if 88 < line_num < 7373:
                if len(list(line)) > 1:
                    if (10 < (len(line)) < 13 and line.strip()[-1] != '”' and line.strip()[-1] != '’' and line.strip()[-1] == '.' and line.strip()[0] == 'C') or 'THE END' in line:
                        chapter_lines.append(line_num)
        line_info = (chapter_lines[chapter_num - 1:chapter_num + 1], chapter_num)
        return line_info

def line_numbers_worlds(chapter_num): # the war of the worlds
    '''

    :param chapter_num: this is the number of the chapter
    :return: this returns the start and end lines of a chapter and the chapter number for the war of the worlds
    '''
    with open('h.g.wells/the_war_of_the_worlds/the_war_of_the_worlds.txt', 'r', encoding='UTF-8') as f:
        line_num = 0
        chapter_lines = []
        for line in f:
            line_num += 1
            if 90 < line_num < 3981:
                if len(list(line)) > 1:
                    if (line.isupper() and len(line) < 7 and line.strip()[-1] != '”' and line.strip()[-1] != '’') or 'BOOK TWO' in line:
                        chapter_lines.append(line_num)
        line_info = (chapter_lines[chapter_num - 1:chapter_num + 1], chapter_num)
        return line_info # i only cut for book 1 in this (there was both books in the file which was confusing but the spec said a novel so yeah)

def line_numbers_sleeper(chapter_num): # when the sleeper wakes
    '''

    :param chapter_num: this is the number of the chapter
    :return: this returns the start and end lines of a chapter and the chapter number for when the sleeper wakes
    '''
    with open('h.g.wells/when_the_sleeper_wakes/when_the_sleeper_wakes.txt', 'r', encoding='UTF-8') as f:
        line_num = 0
        chapter_lines = []
        for line in f:
            line_num += 1
            if 38 < line_num < 9321:
                if len(list(line)) > 1:
                    if (line.isupper() and len(line) > 5 and line.strip()[-1] != '”' and line.strip()[-1] != '’') or 'End of Project Gutenberg’s' in line:
                        chapter_lines.append(line_num)
        line_info = (chapter_lines[chapter_num - 1:chapter_num + 1], chapter_num)
        return line_info

def line_numbers_santa(chapter_num): # the life and adventures of santa claus
    '''

    :param chapter_num: this is the number of the chapter
    :return: this returns the start and end lines of a chapter and the chapter number for the life and adventures of santa claus
    '''
    with open('l.frank.baum/the_life_and_adventures_of_santa_claus/the_life_and_adventures_of_santa_claus.txt', 'r', encoding='UTF-8') as f:
        line_num = 0
        chapter_lines = []
        for line in f:
            line_num += 1
            if 84 < line_num < 9321:
                if len(list(line)) > 1:
                    if (len(line) > 8 and (line.strip()[1] == '.' or line.strip()[1] == '0' or line.strip()[1] == '1' or line.strip()[1] == '2')) or 'End of Project Gutenberg’s' in line:
                        chapter_lines.append(line_num)
        line_info = (chapter_lines[chapter_num - 1:chapter_num + 1], chapter_num)
        return line_info

def line_numbers_wizard(chapter_num): # the wonderful wizard of oz
    '''

    :param chapter_num: this is the number of the chapter
    :return: this returns the start and end lines of a chapter and the chapter number for the wizard of oz
    '''
    with open('l.frank.baum/the_wonderful_wizard_of_oz/the_wonderful_wizard_of_oz.txt', 'r', encoding='UTF-8') as f:
        line_num = 0
        chapter_lines = []
        for line in f:
            line_num += 1
            if 102 < line_num < 4779:
                if len(list(line)) > 1:
                    if (len(line) < 15 and 'Chapter' and line.strip()[-1] == 'I' or line.strip()[-1] == 'V' or line.strip()[-1] == 'X') or 'EBook' in line:
                        chapter_lines.append(line_num)
        line_info = (chapter_lines[chapter_num - 1:chapter_num + 1], chapter_num)
        return line_info

def line_numbers_alice(chapter_num): # alices adventures in wonderland
    '''

    :param chapter_num: this is the number of the chapter
    :return: this returns the start and end lines of a chapter and the chapter number for alice in wonderland
    '''
    with open('lewis.carroll/alices_adventures_in_wonderland/alices_adventures_in_wonderland.txt', 'r', encoding='UTF-8') as f:
        line_num = 0
        chapter_lines = []
        for line in f:
            line_num += 1
            if 55 < line_num < 3407:
                if len(list(line)) > 1:
                    if (len(line) < 15 and line.isupper() and 'Chapter' and line.strip()[-2] == 'I' or line.strip()[-2] == 'V' or line.strip()[-2] == 'X') or 'THE END' in line:
                        chapter_lines.append(line_num)
        line_info = (chapter_lines[chapter_num - 1:chapter_num + 1], chapter_num)
        return line_info

def line_numbers_bruno(chapter_num): # sylvie and bruno
    '''

    :param chapter_num: this is the number of the chapter
    :return: this returns the start and end lines of a chapter and the chapter number for sylvie and bruno
    '''
    with open('lewis.carroll/sylvie_and_bruno/sylvie_and_bruno.txt', 'r', encoding='UTF-8') as f:
        line_num = 0
        chapter_lines = []
        for line in f:
            line_num += 1
            if 118 < line_num < 8366:
                if len(list(line)) > 1:
                    if ((25 < len(line) < 41 or len(line) == 9) and line.isupper() and ('CHAPTER' or 'PREFACE') and (line.strip()[-1] == '.' or line.strip()[-1] == '!')) or 'End of the Project Gutenberg EBook' in line:
                        chapter_lines.append(line_num)
        line_info = (chapter_lines[chapter_num - 1:chapter_num + 1], chapter_num)
        return line_info

def write_file(author, text, list, name):
    '''

    :param list: this is the lines of which the file is written
    :param name: this is the name of the chapter (chapter number)
    :return: this returns a blank file for each chapter to be written to
    '''
    with open(''+author+'/'+text+'/'+name+'.txt', 'w+', encoding='UTF-8') as f:
        for item in list:
            f.write(item)

for i in range(1, 13, 1): # splits and writes chapters for the adventures of sherlock holmes
    chapter_number = line_numbers_sherlock(i) # chapter number
    start_end_lines = (start_end('arthur.conan.doyle', 'sherlock_holmes', 'adventures_sherlock_holmes', chapter_number[0][0], chapter_number[0][1])) # start and end line of each chapter
    write_file('arthur.conan.doyle', 'sherlock_holmes', start_end_lines, 'chapter' + str(i)) # write the chapter into a new file
    if i == 13: # stops when reaches the correct range (needs changing for each novel)
        quit()

for i in range(1, 16, 1): # splits and writes chapters for the hounds of baskervilles
    chapter_number = line_numbers_hounds(i) # chapter number
    start_end_lines = (start_end('arthur.conan.doyle', 'hound_baskervilles', 'the_hound_of_baskervilles', chapter_number[0][0], chapter_number[0][1])) # start and end line of each chapter
    write_file('arthur.conan.doyle', 'hound_baskervilles', start_end_lines, 'chapter' + str(i)) # write the chapter into a new file
    if i == 16: # stops when reaches the correct range (needs changing for each novel)
        quit()

for i in range(1, 18, 1): # splits and writes chapters for the war of the worlds
    chapter_number = line_numbers_worlds(i) # chapter number
    start_end_lines = (start_end('h.g.wells', 'the_war_of_the_worlds', 'the_war_of_the_worlds', chapter_number[0][0], chapter_number[0][1])) # start and end line of each chapter
    write_file('h.g.wells', 'the_war_of_the_worlds', start_end_lines, 'chapter' + str(i)) # write the chapter into a new file
    if i == 18: # stops when reaches the correct range (needs changing for each novel)
        quit()

for i in range(1, 25, 1): # splits and writes chapters for when the sleeper wakes
    chapter_number = line_numbers_sleeper(i) # chapter number
    start_end_lines = (start_end('h.g.wells', 'when_the_sleeper_wakes', 'when_the_sleeper_wakes', chapter_number[0][0], chapter_number[0][1])) # start and end line of each chapter
    write_file('h.g.wells', 'when_the_sleeper_wakes', start_end_lines, 'chapter' + str(i)) # write the chapter into a new file
    if i == 25: # stops when reaches the correct range (needs changing for each novel)
        quit()

for i in range(1, 23, 1): # splits and writes chapters for the life and adventures of santa claus
    chapter_number = line_numbers_santa(i) # chapter number
    start_end_lines = (start_end('l.frank.baum', 'the_life_and_adventures_of_santa_claus', 'the_life_and_adventures_of_santa_claus', chapter_number[0][0], chapter_number[0][1])) # start and end line of each chapter
    write_file('l.frank.baum', 'the_life_and_adventures_of_santa_claus', start_end_lines, 'chapter' + str(i)) # write the chapter into a new file
    if i == 23: # stops when reaches the correct range (needs changing for each novel)
        quit()

for i in range(1, 25, 1): # splits and writes chapters for the wonderful wizard of oz
    chapter_number = line_numbers_wizard(i) # chapter number
    start_end_lines = (start_end('l.frank.baum', 'the_wonderful_wizard_of_oz', 'the_wonderful_wizard_of_oz', chapter_number[0][0], chapter_number[0][1])) # start and end line of each chapter
    write_file('l.frank.baum', 'the_wonderful_wizard_of_oz', start_end_lines, 'chapter' + str(i)) # write the chapter into a new file
    if i == 25: # stops when reaches the correct range (needs changing for each novel)
        quit()

for i in range(1, 13, 1): # splits and writes chapters for alices adventures in wonderland
    chapter_number = line_numbers_alice(i) # chapter number
    start_end_lines = (start_end('lewis.carroll', 'alices_adventures_in_wonderland', 'alices_adventures_in_wonderland', chapter_number[0][0], chapter_number[0][1])) # start and end line of each chapter
    write_file('lewis.carroll', 'alices_adventures_in_wonderland', start_end_lines, 'chapter' + str(i)) # write the chapter into a new file
    if i == 13: # stops when reaches the correct range (needs changing for each novel)
        quit()

for i in range(1, 27, 1): # splits and writes chapters for sylvie and bruno
    chapter_number = line_numbers_bruno(i) # chapter number
    start_end_lines = (start_end('lewis.carroll', 'sylvie_and_bruno', 'sylvie_and_bruno', chapter_number[0][0], chapter_number[0][1])) # start and end line of each chapter
    write_file('lewis.carroll', 'sylvie_and_bruno', start_end_lines, 'chapter' + str(i)) # write the chapter into a new file
    if i == 27: # stops when reaches the correct range (needs changing for each novel)
        quit()


# chapter functions
def chapter_count_sentences(author, text, chapter):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param chapter: this is the chapter from the novel the user wants
    :return: this returns the number of sentences in a certain chapter
    '''
    with open(''+author+'/'+text+'/'+chapter+'.txt', 'r', encoding='UTF-8') as f:
        sentences = [] # create an empty
        count1 = f.read().count('.') # counts number of full stops
        count2 = f.read().count('?') # counts number of question marks
        sentences.append(count1 + count2) # adds these together to get number of sentances
        print(sentences)

def chapter_count_words(author, text, chapter):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param chapter: this is the chapter from the novel the user wants
    :return: this returns the number of words in a certain chapter
    '''
    with open(''+author+'/'+text+'/'+chapter+'.txt', 'r', encoding='UTF-8') as f:
        data = f.read()
        words = data.split(' ') # split into words
        print(len(words))

def chapter_average_sentance(author, text, chapter):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param chapter: this is the chapter from the novel the user wants
    :return: this returns the average sentence length in a certain chapter
    '''
    with open(''+author+'/'+text+'/'+chapter+'.txt', 'r', encoding='UTF-8') as f:
        data = []
        text = f.read()
        sentences = text.split('.')
        for sentence in sentences:
            words = sentence.split(' ')
            data.append(len(words))
        average_wordcount = sum(data) / len(data) # divides the sum of the words by the length
        print(average_wordcount)

def chapter_unique_words(author, text, chapter):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param chapter: this is the chapter from the novel the user wants
    :return: this returns the number of types of words (excluding its repeats) in a certain chapter
    '''
    with open(''+author+'/'+text+'/'+chapter+'.txt', 'r', encoding='UTF-8') as f:
        unique = []
        data = f.read()
        words = data.strip(string.punctuation) # this strips the punctuation from the chapter
        words = words.split()
        for words in words:
            if words not in unique:
                unique.append(words)
        print(unique)
        print(len(unique))

def chapter_frequency_words(author, text, chapter):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param chapter: this is the chapter from the novel the user wants
    :return: this returns the frequency of each word in a certain chapter
    '''
    with open(''+author+'/'+text+'/'+chapter+'.txt', 'r', encoding='UTF-8') as f:
        frequency = {}
        for line in f:
            line = line.strip()
            line = line.strip(string.punctuation)
            line = line.lower()
            line = line.split(' ')
            for word in line:
                word = word.strip()
                if word not in frequency:
                    frequency[word] = 1
                else:
                    frequency[word] += 1
            counts = Counter(frequency) # this counts the frequency of the words in the dictionary
        print(counts)

def chapter_common_words(author, text, chapter):
    '''

    :param name: the name of the chapter (chapter number)
    :return: this returns the words that do not appear in the 10,000 most common words list
    '''
    with open('common_words', 'r') as f1:
        remove = f1.read()
    with open(''+author+'/'+text+'/'+chapter+'.txt', 'r', encoding='UTF-8') as f:
        data = f.read()
        data = data.lower() # lowercase
        words = data.split()
        words = [word.strip('.,!;()[]') for word in words]  # rid of punctuation
        words = [word.replace("'s", '') for word in words]  # singular words
        uncommon_words = []
        for word in words:
            if word in remove:
                uncommon_words.append(word)
    return len(uncommon_words)

# text functions
def text_count_chapters_sherlock(): # counts number of chapters in the adventures of sherlock holmes
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of chapters in a certain novel
    '''
    with open('arthur.conan.doyle/sherlock_holmes/adventures_sherlock_holmes.txt', 'r', encoding='UTF-8') as f:
        for i in range (1,13,1):
            line_numbers_sherlock(i)
        print(i)

def text_count_chapters_hounds(): # counts number of chapters in the hounds of baskerviles
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of chapters in a certain novel
    '''
    with open('arthur.conan.doyle/hound_baskervilles/the_hound_of_baskervilles.txt', 'r', encoding='UTF-8') as f:
        for i in range (1,16,1):
            line_numbers_hounds(i)
        print(i)

def text_count_chapters_worlds(): # counts number of chapters in the war of the worlds
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of chapters in a certain novel
    '''
    with open('h.g.wells/the_war_of_the_worlds/the_war_of_the_worlds.txt', 'r', encoding='UTF-8') as f:
        for i in range (1,18,1):
            line_numbers_hounds(i)
        print(i)

def text_count_chapters_sleeper(): # counts number of chapters in when the sleeper wakes
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of chapters in a certain novel
    '''
    with open('h.g.wells/when_the_sleeper_wakes/when_the_sleeper_wakes.txt', 'r', encoding='UTF-8') as f:
        for i in range (1,25,1):
            line_numbers_hounds(i)
        print(i)

def text_count_chapters_santa(): # counts number of chapters in the life and adventures of santa claus
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of chapters in a certain novel
    '''
    with open('l.frank.baum/the_life_and_adventures_of_santa_claus/the_life_and_adventures_of_santa_claus.txt', 'r', encoding='UTF-8') as f:
        for i in range (1,23,1):
            line_numbers_hounds(i)
        print(i)

def text_count_chapters_wizard(): # counts number of chapters in the wonderful wizard of oz
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of chapters in a certain novel
    '''
    with open('l.frank.baum/the_wonderful_wizard_of_oz/the_wonderful_wizard_of_oz.txt', 'r', encoding='UTF-8') as f:
        for i in range (1,25,1):
            line_numbers_hounds(i)
        print(i)

def text_count_chapters_alice(): # counts number of chapters in alices adventures in wonderland
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of chapters in a certain novel
    '''
    with open('lewis.carroll/alices_adventures_in_wonderland/alices_adventures_in_wonderland.txt', 'r', encoding='UTF-8') as f:
        for i in range (1,13,1):
            line_numbers_hounds(i)
        print(i)

def text_count_chapters_bruno(): # counts number of chapters in sylvie and bruno
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of chapters in a certain novel
    '''
    with open('lewis.carroll/sylvie_and_bruno/sylvie_and_bruno.txt', 'r', encoding='UTF-8') as f:
        for i in range (1,27,1):
            line_numbers_hounds(i)
        print(i)

def text_count_sentances(author, text, file):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of sentences in a certain novel
    '''
    with open (''+author+'/'+text+'/'+file+'.txt', 'r', encoding='UTF-8') as f:
        sentences = []
        count1 = f.read().count('.') # counts number of full stops
        count2 = f.read().count('?') # counts number of quetion marks
        sentences.append(count1 + count2) # appends them to list to have total number of sentances
        print(sentences)

def text_average_sentance(author, text, file):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the average sentence length of a certain novel
    '''
    with open (''+author+'/'+text+'/'+file+'.txt', 'r', encoding='UTF-8') as f:
        data = []
        text = f.read()
        sentences = text.split('.')
        for sentence in sentences:
            words = sentence.split(' ')
            data.append(len(words))
        average_wordcount = sum(data) / len(data) # dividing the amount of sentances by the length of the sentances to get the average
        print(average_wordcount)

def text_unique_words(author, text, file):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the number of types of words (excluding its repeats) in a certain novel
    '''
    with open (''+author+'/'+text+'/'+file+'.txt', 'r', encoding='UTF-8') as f:
        unique = []
        data = f.read()
        words = data.split()
        for words in words:
            if words not in unique: # finds words not already in the list
                unique.append(words)
        print(len(unique))

def text_frequency_words(author, text, file):
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the frequency of the words in a certain novel
    '''
    with open (''+author+'/'+text+'/'+file+'.txt', 'r', encoding='UTF-8') as f:
        frequency = {} # creates a dictionary
        for line in f:
            line = line.strip()
            line = line.strip(string.punctuation) # strips the punctuation
            line = line.lower()
            line = line.split(' ')
            for word in line:
                word = word.strip()
                if word not in frequency:
                    frequency[word] = 1
                else:
                    frequency[word] += 1 # increases the frequency of the word
        print(frequency)

def text_important_words(author, text, file):# doesnt work!!
    '''

    :param author: this is the author of which novel the user wants
    :param text: this is the novel the user wants
    :param file: this is the whole file of the novel (not sliced into chapters)
    :return: this returns the words that are not in the 10,000 most common words
    '''
    with open('common_words', 'r') as f1:
        remove = f1.read()
    with open(''+author+'/'+text+'/'+file+'.txt', 'r', encoding='UTF-8') as f:
        data = f.read()
        data = data.lower()  # makes everything lowercase
        words = data.split()  # splits the text into words
        words = [word.strip('.,!;()[]') for word in words]  # gets rid of punctuation
        words = [word.replace("'s", '') for word in words]  # makes all words singular
        uncommon_words = []
        for word in words:
            if word in remove:
                uncommon_words.append(word)
        print(uncommon_words)
    return len(uncommon_words)

# author functions
def author_unique_words_doyle(): # counts the unique words in the arthur conan doyle novels
    '''

    :return: this returns the number of types of words (excluding its repeats) in the arthur conan doyle novels
    '''
    with open('arthur.conan.doyle/sherlock_holmes/adventures_sherlock_holmes.txt', 'r', encoding='UTF-8') as f1:
        with open('arthur.conan.doyle/hound_baskervilles/the_hound_of_baskervilles.txt', 'r', encoding='UTF-8') as f2:
            unique = []
            data1 = f1.read()
            data2 = f2.read()
            words1 = data1.split()
            words2 = data2.split()
            for words in words1 or words2: # finds words not already in the list unique
                if words not in unique:
                    unique.append(words)
            print(unique)
            print(len(unique))

def author_unique_words_wells(): # counts the unique words in the h.g wells novels
    '''

    :return: this returns the number of types of words (excluding its repeats) in the h.g wells novels
    '''
    with open('h.g.wells/the_war_of_the_worlds/the_war_of_the_worlds.txt', 'r', encoding='UTF-8') as f1:
        with open('h.g.wells/when_the_sleeper_wakes/when_the_sleeper_wakes.txt', 'r', encoding='UTF-8') as f2:
            unique = []
            data1 = f1.read()
            data2 = f2.read()
            words1 = data1.split()
            words2 = data2.split()
            for words in words1 or words2:
                if words not in unique:
                    unique.append(words)
            print(unique)
            print(len(unique))

def author_unique_words_baum(): # counts the unique words in the l.frank baum novels
    '''

    :return: this returns the number of types of words (excluding its repeats) in the l.frank baum novels
    '''
    with open('l.frank.baum/the_life_and_adventures_of_santa_claus/the_life_and_adventures_of_santa_claus.txt', 'r', encoding='UTF-8') as f1:
        with open('l.frank.baum/the_wonderful_wizard_of_oz/the_wonderful_wizard_of_oz.txt', 'r', encoding='UTF-8') as f2:
            unique = []
            data1 = f1.read()
            data2 = f2.read()
            words1 = data1.split()
            words2 = data2.split()
            for words in words1 or words2:
                if words not in unique:
                    unique.append(words)
            print(unique)
            print(len(unique))

def author_unique_words_carroll(): # counts the unique words in the lewis carroll novels
    '''

    :return: this returns the number of types of words (excluding its repeats) in the lewis carroll novels
    '''
    with open('lewis.carroll/alices_adventures_in_wonderland/alices_adventures_in_wonderland.txt', 'r', encoding='UTF-8') as f1:
        with open('lewis.carroll/sylvie_and_bruno/sylvie_and_bruno.txt', 'r', encoding='UTF-8') as f2:
            unique = []
            data1 = f1.read()
            data2 = f2.read()
            words1 = data1.split()
            words2 = data2.split()
            for words in words1 or words2:
                if words not in unique:
                    unique.append(words)
            print(unique)
            print(len(unique))

def author_frequency_words_doyle(): # counts the frequency of each word in the arthur conan doyle novels
    '''

    :return: this returns the frequency of the words in the arthur conan doyle novels
    '''
    with open('arthur.conan.doyle/sherlock_holmes/adventures_sherlock_holmes.txt', 'r', encoding='UTF-8') as f1:
        with open('arthur.conan.doyle/hound_baskervilles/the_hound_of_baskervilles.txt', 'r', encoding='UTF-8') as f2:
            frequency = {}
            for line in f1:
                line = line.strip()
                line = line.strip(string.punctuation)
                line = line.lower()
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    if word not in frequency:
                        frequency[word] = 1
                    else:
                        frequency[word] += 1
            for line in f2:
                line = line.strip()
                line = line.strip(string.punctuation)
                line = line.lower()
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    if word not in frequency:
                        frequency[word] = 1
                    else:
                        frequency[word] += 1
            print(frequency)

def author_frequency_words_wells(): # counts the frequency of each word in the h.g wells novels
    '''

    :return: this returns the frequency of the words in the h.g wells novels
    '''
    with open('h.g.wells/the_war_of_the_worlds/the_war_of_the_worlds.txt', 'r', encoding='UTF-8') as f1:
        with open('h.g.wells/when_the_sleeper_wakes/when_the_sleeper_wakes.txt', 'r', encoding='UTF-8') as f2:
            frequency = {}
            for line in f1:
                line = line.strip()
                line = line.strip(string.punctuation)
                line = line.lower()
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    if word not in frequency:
                        frequency[word] = 1
                    else:
                        frequency[word] += 1
            for line in f2:
                line = line.strip()
                line = line.strip(string.punctuation)
                line = line.lower()
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    if word not in frequency:
                        frequency[word] = 1
                    else:
                        frequency[word] += 1
            print(frequency)

def author_frequency_words_baum(): # counts the frequency of each word in the l.frank baum novels
    '''

    :return: this returns the frequency of the words in the l.frank baum novels
    '''
    with open('l.frank.baum/the_life_and_adventures_of_santa_claus/the_life_and_adventures_of_santa_claus.txt', 'r', encoding='UTF-8') as f1:
        with open('l.frank.baum/the_wonderful_wizard_of_oz/the_wonderful_wizard_of_oz.txt', 'r', encoding='UTF-8') as f2:
            frequency = {}
            for line in f1:
                line = line.strip()
                line = line.strip(string.punctuation)
                line = line.lower()
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    if word not in frequency:
                        frequency[word] = 1
                    else:
                        frequency[word] += 1
            for line in f2:
                line = line.strip()
                line = line.strip(string.punctuation)
                line = line.lower()
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    if word not in frequency:
                        frequency[word] = 1
                    else:
                        frequency[word] += 1
            print(frequency)

def author_frequency_words_carroll(): # counts the frequency of each word in the lewis carroll novels
    '''

    :return: this returns the frequency of the words in the lewis carroll novels
    '''
    with open('lewis.carroll/alices_adventures_in_wonderland/alices_adventures_in_wonderland.txt', 'r', encoding='UTF-8') as f1:
        with open('lewis.carroll/sylvie_and_bruno/sylvie_and_bruno.txt', 'r', encoding='UTF-8') as f2:
            frequency = {}
            for line in f1:
                line = line.strip()
                line = line.strip(string.punctuation)
                line = line.lower()
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    if word not in frequency:
                        frequency[word] = 1
                    else:
                        frequency[word] += 1
            for line in f2:
                line = line.strip()
                line = line.strip(string.punctuation)
                line = line.lower()
                line = line.split(' ')
                for word in line:
                    word = word.strip()
                    if word not in frequency:
                        frequency[word] = 1
                    else:
                        frequency[word] += 1
            print(frequency)

def author_common_words_doyle(): # the number of uncommon words in the arthur conan doyle novels
    '''

    :return: this returns the words that are not in the 10,000 most common words
    '''
    with open('common_words', 'r') as f1:
        remove = f1.read()
    with open('arthur.conan.doyle/sherlock_holmes/adventures_sherlock_holmes.txt', 'r', encoding='UTF-8') as f1:
        with open('arthur.conan.doyle/hound_baskervilles/the_hound_of_baskervilles.txt', 'r', encoding='UTF-8') as f2:
            data1 = f1.read()
            data2 = f2.read()
            data1 = data1.lower()  # makes everything lowercase
            data2 = data2.lower()
            words1 = data1.split()  # splits the text into words
            words1 = [word.strip('.,!;()[]') for word in words1]  # gets rid of punctuation
            words1 = [word.replace("'s", '') for word in words1]  # makes all words singular
            words2 = data2.split()
            words2 = [word.strip('.,!;()[]') for word in words2]
            words2 = [word.replace("'s", '') for word in words2]
            uncommon_words = []
            for word in words1:
                if word in remove:
                    uncommon_words.append(word)
            for word in words2:
                if word in remove:
                    uncommon_words.append(word)
        return len(uncommon_words)

def author_common_words_wells(): # the number of uncommon words in the h.g. wells novels
    '''

    :return: this returns the words that are not in the 10,000 most common words
    '''
    with open('common_words', 'r') as f1:
        remove = f1.read()
    with open('h.g.wells/the_war_of_the_worlds/the_war_of_the_worlds.txt', 'r', encoding='UTF-8') as f1:
        with open('h.g.wells/when_the_sleeper_wakes/when_the_sleeper_wakes.txt', 'r', encoding='UTF-8') as f2:
            data1 = f1.read()
            data2 = f2.read()
            data1 = data1.lower()  # makes everything lowercase
            data2 = data2.lower()
            words1 = data1.split()  # splits the text into words
            words1 = [word.strip('.,!;()[]') for word in words1]  # gets rid of punctuation
            words1 = [word.replace("'s", '') for word in words1]  # makes all words singular
            words2 = data2.split()
            words2 = [word.strip('.,!;()[]') for word in words2]
            words2 = [word.replace("'s", '') for word in words2]
            uncommon_words = []
            for word in words1:
                if word in remove:
                    uncommon_words.append(word)
            for word in words2:
                if word in remove:
                    uncommon_words.append(word)
        return len(uncommon_words)

def author_common_words_baum(): # the number of uncommon words in the l.frank baum novels
    '''

    :return: this returns the words that are not in the 10,000 most common words
    '''
    with open('common_words', 'r') as f1:
        remove = f1.read()
    with open('l.frank.baum/the_life_and_adventures_of_santa_claus/the_life_and_adventures_of_santa_claus.txt', 'r', encoding='UTF-8') as f1:
        with open('l.frank.baum/the_wonderful_wizard_of_oz/the_wonderful_wizard_of_oz.txt', 'r', encoding='UTF-8') as f2:
            data1 = f1.read()
            data2 = f2.read()
            data1 = data1.lower()  # makes everything lowercase
            data2 = data2.lower()
            words1 = data1.split()  # splits the text into words
            words1 = [word.strip('.,!;()[]') for word in words1]  # gets rid of punctuation
            words1 = [word.replace("'s", '') for word in words1]  # makes all words singular
            words2 = data2.split()
            words2 = [word.strip('.,!;()[]') for word in words2]
            words2 = [word.replace("'s", '') for word in words2]
            uncommon_words = []
            for word in words1:
                if word in remove:
                    uncommon_words.append(word)
            for word in words2:
                if word in remove:
                    uncommon_words.append(word)
        return len(uncommon_words)

def author_common_words_carroll(): # the number of uncommon words in the lewis carroll novels
    '''

    :return: this returns the words that are not in the 10,000 most common words
    '''
    with open('common_words', 'r') as f1:
        remove = f1.read()
    with open('lewis.carroll/alices_adventures_in_wonderland/alices_adventures_in_wonderland.txt', 'r', encoding='UTF-8') as f1:
        with open('lewis.carroll/sylvie_and_bruno/sylvie_and_bruno.txt', 'r', encoding='UTF-8') as f2:
            data1 = f1.read()
            data2 = f2.read()
            data1 = data1.lower()  # makes everything lowercase
            data2 = data2.lower()
            words1 = data1.split()  # splits the text into words
            words1 = [word.strip('.,!;()[]') for word in words1]  # gets rid of punctuation
            words1 = [word.replace("'s", '') for word in words1]  # makes all words singular
            words2 = data2.split()
            words2 = [word.strip('.,!;()[]') for word in words2]
            words2 = [word.replace("'s", '') for word in words2]
            uncommon_words = []
            for word in words1:
                if word in remove:
                    uncommon_words.append(word)
            for word in words2:
                if word in remove:
                    uncommon_words.append(word)
        return len(uncommon_words)

# graphs
def chapter_graph():
    '''

    :return: this returns a horizontal bar graph which shows the number of chapters in each novel
    '''
    chapter_chart = pygal.HorizontalBar()
    chapter_chart.title = 'Number of Chapters in each Novel'
    chapter_chart.add('The Adventures of Sherlock Holmes', 12)
    chapter_chart.add('The Hound of Baskervilles', 15)
    chapter_chart.add('The War of the Worlds', 17)
    chapter_chart.add('When the Sleeper Wakes', 24)
    chapter_chart.add('The Life and Adventures of Santa Claus', 22)
    chapter_chart.add('The Wonderful Wizard of Oz', 24)
    chapter_chart.add('Alices Adventures in Wonderland', 12)
    chapter_chart.add('Sylvie and Bruno', 26)
    print(chapter_chart.render_to_file('graphs/chapter.chart.svg'))

def average_sentance_graph():
    '''

    :return: this returns a bar graph which shows the average sentance length of each novel
    '''
    sentance_chart = pygal.Bar()
    sentance_chart.title = 'Average Sentence Length in each Novel'
    sentance_chart.add('The Adventures of Sherlock Holmes', 16.297948399129623)
    sentance_chart.add('The Hound of Baskervilles', 26.19906900328587)
    sentance_chart.add('The War of the Worlds', 18.05558840922531)
    sentance_chart.add('When the Sleeper Wakes', 14.304011017386813)
    sentance_chart.add('The Life and Adventures of Santa Claus', 21.303326810176124)
    sentance_chart.add('The Wonderful Wizard of Oz', 18.797722095671983)
    sentance_chart.add('Alices Adventures in Wonderland', 23.39087947882736)
    sentance_chart.add('Sylvie and Bruno', 19.390017411491584)
    print(sentance_chart.render_to_file('graphs/sentance.chart.svg'))

def number_words_graphs():
    '''

    :return: this returns a horizontal bar graph which shows the number of words per novel
    '''
    words_chart = pygal.HorizontalBar()
    words_chart.title = 'Number of Words per Novel'
    words_chart.add('The Adventures of Sherlock Holmes', 98428)
    words_chart.add('The Hound of Baskervilles', 92028)
    words_chart.add('The War of the Worlds', 57683)
    words_chart.add('When the Sleeper Wakes', 77284)
    words_chart.add('The Life and Adventures of Santa Claus', 31126)
    words_chart.add('The Wonderful Wizard of Oz', 39067)
    words_chart.add('Alices Adventures in Wonderland', 27497)
    words_chart.add('Sylvie and Bruno', 63373)
    print(words_chart.render_to_file('graphs/words_text.chart.svg'))

def words_chapter_graph():
    '''

    :return: this returns a line graph which shows the number of words in each chapter in each novel
    '''
    chapter_words_chart = pygal.Line()
    chapter_words_chart.title = 'Number of Words per Chapter per Novel'
    chapter_words_chart.x_labels = map(str, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                                             '15', '16', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'))
    chapter_words_chart.add('The Adventures of Sherlock Holmes', [7830, 8301, 6372, 8790, 6666, 8392, 7107, 8930, 7564,
                                                                  7415, 8885, 9194, None, None, None, None, None, None, None,
                                                                   None, None, None, None, None, None, None])
    chapter_words_chart.add('The Hound of Baskervilles',  [3398, 6991, 4500, 6123, 5203, 5167, 7359, 3996, 9680, 5361, 6752,
                                                           7235, 5162, 6137, 5913, None, None, None, None, None, None, None,
                                                           None, None, None, None])
    chapter_words_chart.add('The War of the Worlds',      [2026, 1217, 922, 1013, 1347, 764, 1197, 885, 1933, 2064, 1847,
                                                           3487, 1598, 3376, 2555, 3980, 2979, None, None, None, None, None,
                                                           None, None, None, None])
    chapter_words_chart.add('When the Sleeper Wakes',  [2325, 1849, 1313, 3718, 1332, 2668, 3392, 3925, 1803, 3593, 3348,
                                                        1069, 4404, 1254, 4803, 3524, 4347, 1712, 2493, 2085, 6166, 2063,
                                                        3795, 4787, 3674, None, None])
    chapter_words_chart.add('The Life and Adventures of Santa Claus', [212, 1329, 386, 921, 598, 928, 872, 1495, 1106, 1923,
                                                                       3295, 1738, 1777, 1624, 2289, 404, 1957, 1769, 966,
                                                                       2201, 887, 1585, None, None, None, None])
    chapter_words_chart.add('The Wonderful Wizard of Oz',  [1050, 1830, 1789, 1315, 1891, 1367, 1654, 1765, 1268, 1790,
                                                            1705, 3362, 1090, 1723, 2519, 840, 1059, 1063, 929, 1378, 821,
                                                            852, 1142, 71, None, None])
    chapter_words_chart.add('Alices Adventures in Wonderland',      [2182, 1953, 1609, 2400, 2126, 2374, 2075, 2256, 2048,
                                                                     1848, 1939, None, None, None, None, None, None, None,
                                                                   None, None, None, None, None, None, None])
    chapter_words_chart.add('Sylvie and Bruno',  [2036, 1903, 2003, 1755, 2454, 1957, 1669, 1743, 2154, 1871, 2037, 2099,
                                                  2288, 3304, 2308, 1779, 2948, 2318, 2445, 2549, 3000, 3086, 2528, 3162,
                                                  1984, 3015])
    print(chapter_words_chart.render_to_file('graphs/words_chapter.chart.svg'))

def special_words_graph():
    '''

    :return: this returns a bar graph which shows the number of words not in the 10,00 most common words (uncommon words) for each author
    '''
    sentance_chart = pygal.Bar()
    sentance_chart.title = 'Number of Words Not in the 10,000 Most Common Words per Author'
    sentance_chart.add('Arthur Conan Doyle', 145816)
    sentance_chart.add('H.G Wells', 123710)
    sentance_chart.add('L.Frank Baum', 65184)
    sentance_chart.add('Lewis Carroll', 78102)
    print(sentance_chart.render_to_file('graphs/special_words.chart.svg'))