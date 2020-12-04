# 1.i
# import re
# string = 'simple@example.com this is simple email ' \
#          'very.common@example.com this is common email ' \
#          'disposable.style.email.with+symbol@example.com ' \
#          'other.email-with-hyphen@example.com ' \
#          'fully-qualified-domain@example.com ' \
#          'user.name+tag+sorting@example.com ' \
#          'x@example.com ' \
#          'example-indeed@strange-example.com ' \
#          'admin@mailserver1 this is top level domain ' \
#          'yu@example.org ' \
#          'mailhost!username@example.org ' \
#          'user%example.com@example.org '
# lst = re.findall(r"[\w%&+-]?\S+@\S+", string)
# print(lst)

# Output:
# ['simple@example.com', 'very.common@example.com', 'disposable.style.email.with+symbol@example.com', 'other.email-with-hyphen@example.com', 'fully-qualified-domain@example.com', 'user.name+tag+sorting@example.com', 'x@example.com', 'example-indeed@strange-example.com', 'admin@mailserver1', 'yu@example.org', 'mailhost!username@example.org', 'user%example.com@example.org']
#
# 1.ii
# import re
# txt_file = open("abc.txt")
# txt = txt_file.read()
# string = re.findall(r"[\w%&+-]?\S+@\S+", txt)
# print(string)

# Output:
# ['simple@example.com', 'very.common@example.com', 'disposable.style.email.with+symbol@example.com', 'other.email-with-hyphen@example.com', 'fully-qualified-domain@example.com', 'user.name+tag+sorting@example.com', 'user.name@example.com', 'x@example.com', 'example-indeed@strange-example.com', 'admin@mailserver1', 'example@s.example', '"john..doe"@example.org', 'mailhost!username@example.org', 'user%example.com@example.org', 'user@example.com']

# 2.i
# a Python program to extract Telephone numbers present in a string
# import re
# string = "+91 9856121133 " \
#          "+11 70051-54879 " \
#          "0 96152 56365 " \
#          "0 9089256321 " \
#          "70051 42456 " \
#          "55555-66666 " \
#          "8787760746"
# telephone number are given format can be extract from any string.
# phone = re.findall(r'\D?\d{,2}\D?\d{5}\D?\d{5}|\d{10}', string)
# for i, phone_num in enumerate(phone, start=1):
#     print(i, phone_num)

# Output:
# 1 +91 9856121133
# 2 +11 70051-54879
# 3  0 96152 56365
# 4  0 9089256321
# 5  70051 42456
# 6  55555-66666
# 7  8787760746


# 2.ii
# import re
# ph_dir_file = open("phone_no.txt")
# txt = ph_dir_file.read()
# phone = re.findall(r'\D?\d{,2}\D?\d{5}\D?\d{5}|\d{10}', txt)
# print(phone)

# Output
# ['+91 9856121133', '+11 70051-54879', ' 0 96152 56365', ' 0 9089256321', ' 70051 42456', ' 55555-66666', ' 8787760746']

# 3.i
# import re
# html_code = '''
# <html>
# <head>
# <title>Remove html tag</title>
# </head>
# <body>
# Hi i removed html tag using python
# </body>
# </html>
# '''
# pattern = re.compile(r'<.+?>')
# text = pattern.sub('',html_code)
# print(text)

# output:
# Hi i removed html tag using python

# 3.ii
# import re
# html_file = open('remove tag.html')
# html_code = html_file.read()
# pattern = re.compile(r'<.+?>')
# text = pattern.sub('', html_code)
# print(text)

# Output:
# Hi i removed html tag using python from html file

# 4
# from datetime import date
#
# date_1 = date(year=2020, month=11, day=23)
# date_2 = date(year=2021, month=1, day=15)
#
# date_cal = date_2 - date_1
# number_of_days = date_cal.days
#
# print("\nDate difference: ", number_of_days,"days")
#
# Output:
# Date difference:  53 days

# 5
# from stopword import stopword
# import re
# import time
#
#
# regex = re.compile('^a-zA-Z')
#
# txt_file = open("clown.txt")
# txt = txt_file.read()
# txt_file.close()
#
# words = txt.split()
# word_freq = {}
#
# time1 = time.time()
#
# for word in words:
#     word = regex.sub('', word)
#     word = word.lower()
#     if not stopword(word):
#         word_freq[word] = word_freq.get(word, 0)+1
# sort_word_freq = {k: v for k, v in sorted(word_freq.items(), key=lambda item: item[1], reverse=True)}
#
#
# time2 = time.time()
# print(sort_word_freq)
# print("Different time :", time2 - time1, " secs")

# Output:
# {'one': 4, 'holmes': 3, 'upon': 3, 'case': 3, 'always': 2, 'seldom': 2, 'heard': 2, 'whole': 2, 'emotion': 2, 'irene': 2, 'woman': 2, 'little': 2, 'every': 2, 'baker': 2, 'week': 2, 'keen': 2, 'study': 2, 'extraordinary': 2, 'clearing': 2, 'time': 2, 'singular': 2, 'knew': 2, 'dark': 2, 'see': 2, 'looked': 2, 'manner': 2, 'sherlock': 1, '_the_': 1, 'woman.': 1, 'mention': 1, 'name.': 1, 'eyes': 1, 'eclipses': 1, 'predominates': 1, 'sex.': 1, 'felt': 1, 'akin': 1, 'love': 1, 'adler.': 1, 'emotions,': 1, 'particularly,': 1, 'abhorrent': 1, 'cold,': 1, 'precise': 1, 'admirably': 1, 'balanced': 1, 'mind.': 1, 'was,': 1, 'take': 1, 'it,': 1, 'perfect': 1, 'reasoning': 1, 'observing': 1, 'machine': 1, 'world': 1, 'seen,': 1, 'lover': 1, 'placed': 1, 'false': 1, 'position.': 1, 'never': 1, 'spoke': 1, 'softer': 1, 'passions,': 1, 'save': 1, 'gibe': 1, 'sneer.': 1, 'admirable': 1, 'things': 1, 'observerâ€”excellent': 1, 'drawing': 1, 'veil': 1, 'menâ€™s': 1, 'motives': 1, 'actions.': 1, 'trained': 1, 'reasoner': 1, 'admit': 1, 'intrusions': 1, 'delicate': 1, 'finely': 1, 'adjusted': 1, 'temperament': 1, 'introduce': 1, 'distracting': 1, 'factor': 1, 'might': 1, 'throw': 1, 'doubt': 1, 'mental': 1, 'results.': 1, 'grit': 1, 'sensitive': 1, 'instrument,': 1, 'crack': 1, 'high-power': 1, 'lenses,': 1, 'disturbing': 1, 'strong': 1, 'nature': 1, 'his.': 1, 'yet': 1, 'him,': 1, 'late': 1, 'adler,': 1, 'dubious': 1, 'questionable': 1, 'memory.': 1, 'seen': 1, 'lately.': 1, 'marriage': 1, 'drifted': 1, 'us': 1, 'away': 1, 'other.': 1, 'complete': 1, 'happiness,': 1, 'home-centred': 1, 'interests': 1, 'rise': 1, 'around': 1, 'man': 1, 'first': 1, 'finds': 1, 'master': 1, 'establishment,': 1, 'sufficient': 1, 'absorb': 1, 'attention,': 1, 'holmes,': 1, 'loathed': 1, 'form': 1, 'society': 1, 'bohemian': 1, 'soul,': 1, 'remained': 1, 'lodgings': 1, 'street,': 1, 'buried': 1, 'among': 1, 'old': 1, 'books,': 1, 'alternating': 1, 'cocaine': 1, 'ambition,': 1, 'drowsiness': 1, 'drug,': 1, 'fierce': 1, 'energy': 1, 'nature.': 1, 'still,': 1, 'ever,': 1, 'deeply': 1, 'attracted': 1, 'crime,': 1, 'occupied': 1, 'immense': 1, 'faculties': 1, 'powers': 1, 'observation': 1, 'following': 1, 'clues,': 1, 'mysteries': 1, 'abandoned': 1, 'hopeless': 1, 'official': 1, 'police.': 1, 'vague': 1, 'account': 1, 'doings:': 1, 'summons': 1, 'odessa': 1, 'trepoff': 1, 'murder,': 1, 'tragedy': 1, 'atkinson': 1, 'brothers': 1, 'trincomalee,': 1, 'finally': 1, 'mission': 1, 'accomplished': 1, 'delicately': 1, 'successfully': 1, 'reigning': 1, 'family': 1, 'holland.': 1, 'beyond': 1, 'signs': 1, 'activity,': 1, 'however,': 1, 'merely': 1, 'shared': 1, 'readers': 1, 'daily': 1, 'press,': 1, 'former': 1, 'friend': 1, 'companion.': 1, 'nightâ€”it': 1, 'twentieth': 1, 'march,': 1, '1888â€”i': 1, 'returning': 1, 'journey': 1, 'patient': 1, '(for': 1, 'returned': 1, 'civil': 1, 'practice),': 1, 'way': 1, 'led': 1, 'street.': 1, 'passed': 1, 'well-remembered': 1, 'door,': 1, 'must': 1, 'associated': 1, 'mind': 1, 'wooing,': 1, 'incidents': 1, 'scarlet,': 1, 'seized': 1, 'desire': 1, 'again,': 1, 'know': 1, 'employing': 1, 'powers.': 1, 'rooms': 1, 'brilliantly': 1, 'lit,': 1, 'and,': 1, 'even': 1, 'up,': 1, 'saw': 1, 'tall,': 1, 'spare': 1, 'figure': 1, 'pass': 1, 'twice': 1, 'silhouette': 1, 'blind.': 1, 'pacing': 1, 'room': 1, 'swiftly,': 1, 'eagerly,': 1, 'head': 1, 'sunk': 1, 'chest': 1, 'hands': 1, 'clasped': 1, 'behind': 1, 'him.': 1, 'me,': 1, 'mood': 1, 'habit,': 1, 'attitude': 1, 'told': 1, 'story.': 1, 'work': 1, 'again.': 1, 'risen': 1, 'drug-created': 1, 'dreams': 1, 'hot': 1, 'scent': 1, 'new': 1, 'problem.': 1, 'rang': 1, 'bell': 1, 'shown': 1, 'chamber': 1, 'formerly': 1, 'part': 1, 'own.': 1, 'effusive.': 1, 'was;': 1, 'glad,': 1, 'think,': 1, 'me.': 1, 'hardly': 1, 'word': 1, 'spoken,': 1, 'kindly': 1, 'eye,': 1, 'waved': 1, 'armchair,': 1, 'threw': 1, 'across': 1, 'cigars,': 1, 'indicated': 1, 'spirit': 1, 'gasogene': 1, 'corner.': 1, 'stood': 1, 'fire': 1, 'introspective': 1, 'fashion.': 1}
# Different time : 0.001995086669921875  secs


# 6.a
# Python program to explain os.mkdir() method
# import os,glob,shutil
# directory = "python_programs"
# # Parent Directory path
# parent_dir = "C:/Users/Athokpam Trendy/Desktop/"
# path = os.path.join(parent_dir, directory)
# os.mkdir(path)
# print("Directory '% s' created" % directory)
# os.chdir('C:/Users/Athokpam Trendy/Desktop')
# for file in glob.glob('*.py'):
#     print(file)
#     shutil.copy(file, directory)
# print("All (.py) extension files are copied to python_programs folder...")

# Output:
# Directory 'python_programs' created
# assignment test.py
# rarcrack.py
# wish.py
# All (.py) extension files are copied to python_programs folder...

# 6.b
# import zipfile,os
# fantasy_zip = zipfile.ZipFile('C:/Users/Athokpam Trendy/Desktop/python_programs.zip', 'w')
# for folder, subfolders, files in os.walk('C:/Users/Athokpam Trendy/Desktop/python_programs'):
#
#     for file in files:
#         if file.endswith('.py'):
#             fantasy_zip.write(os.path.join(folder, file),
#                               os.path.relpath(os.path.join(folder, file), 'C:/Users/Athokpam Trendy/Desktop/python_programs'),
#                               compress_type=zipfile.ZIP_DEFLATED)
#             print(file)
#
# fantasy_zip.close()
# print("All files are compress as a zip file")

# Output:
# assignment test.py
# rarcrack.py
# wish.py
# All files are compress as a zip file

# 6.c
import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['allsoftware999@gmail.com', 'foreignhacker@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = 'trendysback@gmail.com'
msg['To'] = 'tajathokpam@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
