import praw
import smtplib

title='Hardware bot Deals'
content=""
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('hardwaresalesbot@gmail.com', '********')

reddit=praw.Reddit(client_id='LUdXtwAMitap8A', client_secret='qQfMU7Vq7grR_Oshnef8f7_MlmQ', user_agent='hardwarescraper')

hardwareswap=reddit.subreddit('hardwareswap')

content+=('***************\n')
content+=('***GTX 1070***\n')
content+=('***************\n')
for submission in hardwareswap.search('title:"USA-MA" flair:"selling" 1070', sort='new', limit=5):
    content+=(submission.title + '\n')
    content+=(submission.url + '\n')
    content+=(submission.selftext + '\n')
    content+=('\n******************************************************************\n')
content+=('***************\n')
content+=('***GTX 1080***\n')
content+=('***************\n')
for submission in hardwareswap.search('title:"USA-MA" flair:"selling" 1080', sort='new', limit=5):
    content+=(submission.title + '\n')
    content+=(submission.url + '\n')
    content+=(submission.selftext + '\n')
    content+=('\n******************************************************************\n')
content+=('***************\n')
content+=('***i5 4670k***\n')
content+=('***************\n')
for submission in hardwareswap.search('title:"USA-MA" flair:"selling" 4670k', sort='new', limit=5):
    content+=(submission.title + '\n')
    content+=(submission.url + '\n')
    content+=(submission.selftext + '\n')
    content+=('\n******************************************************************\n')
content+=('***************\n')
content+=('***i5 4690k***\n')
content+=('***************\n')
for submission in hardwareswap.search('title:"USA-MA" flair:"selling" 4690k', sort='new', limit=5):
    content+=(submission.title + '\n')
    content+=(submission.url + '\n')
    content+=(submission.selftext + '\n')
    content+=('\n******************************************************************\n')
content+=('***************\n')
content+=('***i7 4770k***\n')
content+=('***************\n')
for submission in hardwareswap.search('title:"USA-MA" flair:"selling" 4770k', sort='new', limit=5):
    content+=(submission.title + '\n')
    content+=(submission.url + '\n')
    content+=(submission.selftext + '\n')
    content+=('\n******************************************************************\n')
content+=('***************\n')
content+=('***i7 4790k***\n')
content+=('***************\n')
for submission in hardwareswap.search('title:"USA-MA" flair:"selling" 4790k', sort='new', limit=5):
    content+=(submission.title + '\n')
    content+=(submission.url + '\n')
    content+=(submission.selftext + '\n')
    content+=('\n******************************************************************\n')

#print(content)
mail.sendmail('hardwaresalesbot@gmail', 'fairfaxk@wit.edu', content.encode('utf-8'))
mail.close()
