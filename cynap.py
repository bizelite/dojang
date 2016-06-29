names = '''이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'''

name_list = names.split(',')

#1
print('김 : {}'.format(len([name for name in name_list if name[0] == '김'])))
print('이 : {}'.format(len([name for name in name_list if name[0] == '이'])))

#2
print(name_list.count('이재영'))

#3
print(list(set(name_list)))

#4
print(sorted(list(set(name_list))))