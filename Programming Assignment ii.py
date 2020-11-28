# #1.i
import re
string = 'simple@example.com ' \
         'very.common@example.com ' \
         'disposable.style.email.with+symbol@example.com ' \
         'other.email-with-hyphen@example.com ' \
         'fully-qualified-domain@example.com ' \
         'user.name+tag+sorting@example.com ' \
         'x@example.com ' \
         'example-indeed@strange-example.com ' \
         'admin@mailserver1 ' \
         '" "example.org ' \
         'yu@example.org ' \
         'mailhost!username@example.org ' \
         'user%example.com@example.org '
lst = re.findall(r"[\w%&+-]+[^.< ]"
                 r"[\w%&+.-]+@[\w.-]+"
                 r"[com$net$in$org$edu$uk$fr$br$de$ru$it$es$ca$jp$nl$be$au$sg$nl$ch$]{2,4}", string)
print(lst)

#1.ii
# import re
# txt_file = open("abc.txt")
# txt = txt_file.read()
# string = re.findall(r"[A-Za-z0-9._%+-]+"
#                      r"@[A-Za-z0-9.-]+"
#                      r"\.[A-Za-z]{2,4}", txt)
# print(string)

# import re
# txt_file = open("abc.txt")
# txt = txt_file.read()
# string = re.findall(r"[^.<]"
#                     r"[\w%&+.-]+"
#                     r"@[\w.-]+"
#                     r"\.[com$net$in$org$edu$uk$fr$br$de$ru$it$es$ca$jp$nl$be$au$sg$nl$ch$]{2,4}", txt)
# print(string)
# removing duplicated from list
# using naive methods
# res = []
# for i in string:
#     if i not in res:
#         res.append(i)
# res.sort()
# print(res)
