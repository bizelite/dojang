name_list = ['이유덕','이재영','권종표','이재영','박민호','강상희', \
             '이재영','김지완','최승혁','이성연','박영서','박민호', \
             '전경헌','송정환','김재성','이유덕','전경헌']


if __name__ == '__main__':
    # 김씨와 이씨는 각각 몇 명 인가요?
    kim_count = 0
    lee_count = 0

    for name in name_list:
        if name.startswith('김'):
            kim_count += 1
        elif name.startswith('이'):
            lee_count += 1
        else:
            continue

    print('Kim\'s Count:', kim_count)
    print('Lee\'s Count:', lee_count)


    # "이재영"이란 이름이 몇 번 반복되나요?
    print(name_list.count('이재영'))


    # 중복을 제거한 이름을 출력하세요.
    print(set(name_list))

    # 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
    print(sorted(set(name_list)))


