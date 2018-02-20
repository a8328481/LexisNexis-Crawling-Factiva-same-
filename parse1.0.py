import pandas as pd

from os import listdir
import os
import sqlite3

mypath = "C:\Users\lhuang54\Downloads"
os.chdir(mypath)
onlyfiles = open('C:\Users\lhuang54\PycharmProjects\Parse file\\files.csv','r').read().split('\n')
df = pd.DataFrame()
count = 0
while True:
    for filename in onlyfiles[0:10]:
        print filename
        my_text = open(filename).read().split('DOCUMENTS')
        company = []
        start_position = my_text[0].find('NOTE')
        end_position = my_text[0].find('\n', start_position)
        company_name = my_text[0][start_position + 5:end_position]
        year = []
        date = []
        month = []
        source = []
        content = []
        word_length = []
        title = []
        size = len(my_text)
        df1 = pd.DataFrame()
        for news in my_text[1:]:
            print news
            date_start_position = news.find("LOAD-DATE:")
            if date_start_position < 0:
                date_start_position = news.find("UPDATE:")
                date_end_position = news.find("\n", date_start_position)
                try:
                    year.append(news[date_start_position + 11:date_end_position].split()[1].rstrip().decode('utf-8'))
                except:
                    year.append(news[date_start_position + 11:date_end_position].decode('utf-8'))
                M = year[-1]
                month.append(news[date_start_position + 11:date_end_position].split()[0].decode('utf-8'))
                date.append("null")
            else:
                date_end_position = news.find("\n", date_start_position)
                try:
                    year.append(news[date_start_position + 11:date_end_position].split(',')[1][0:5].decode('utf-8'))
                except:
                    year.append(news[date_start_position + 11:date_end_position].split(',')[0][0:5].decode('utf-8'))
                try:
                    date.append(news[date_start_position + 11:date_end_position].split(',')[0].split()[1].decode('utf-8'))
                except:
                    date.append("null")
                M = year[-1]
                month.append(news[date_start_position + 11:date_end_position].split(',')[0].split()[0].decode('utf-8'))

            index = news.find(str(M))
            #source.append(news[:index - 25].replace('\n', '').rstrip().decode('utf-8'))
            try:
                length_start_position = news.find("LENGTH:") + 7
                length_end_position = length_start_position + news[length_start_position:].find('\n')
                word_length.append(news[length_start_position:length_end_position].split()[0].decode('utf-8'))
            except:
                word_length.append('null')
            content.append(news.replace('\n', ' ').decode('utf-8'))
            company.append(company_name)
            for s in range(0,len(news.split('\n\n'))):
                if len(news.split('\n\n')[s])>1:
                    source.append(news.split('\n\n')[s].strip().decode('utf-8'))
                    break
            for s in range(0, len(news.split('\n\n'))):
                if str(year[-1]) in news.split('\n\n')[s]:
                    try:
                        title.append(news.split('\n\n')[s+1].decode('utf-8'))
                    except:
                        title.append('null')
                    break




        df1['year'] = year
        df1['month'] = month
        df1['date'] = date
        df1['source'] = source
        df1['word_length'] = word_length
        df1['content'] = content
        df1['name'] = company
        df1['title'] = title

        df = df.append(df1, ignore_index=True)

        conn = sqlite3.connect('C:\Users\lhuang54\example1.sqlite')
        cur = conn.cursor()
        # Make some fresh tables using executescript()
        cur.executescript('''
        CREATE TABLE IF NOT EXISTS NewsArticle (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            Name  Text,
            Year  Text,
            month  Text,
            Day  Text,
            Source Text,
            Content Text,
            Words  Text,
            Title  Text
            );
        ''')
        for i in range(0, len(df) - 1):
            cur.execute('''INSERT OR IGNORE INTO NewsArticle (Name, Year, month, Day, Source, Content, Words, Title)
                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)''', (
            df['name'][i], df['year'][i], df['month'][i], df['date'][i], df['source'][i], df['content'][i],
            df['word_length'][i], df['title'][i]))
        conn.commit()
        conn.close()
        with open('C:\Users\lhuang54\PycharmProjects\Parse file\\files.csv', 'w') as f:
            for i in onlyfiles[10:]:
                f.write(i + '\n')
        onlyfiles = open('C:\Users\lhuang54\PycharmProjects\Parse file\\files.csv', 'r').read().split('\n')
        count += 1

print count