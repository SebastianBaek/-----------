# https://school.programmers.co.kr/learn/courses/30/lessons/155651
def solution(book_time):
    for i in range(len(book_time)):
        for j in range(2):
            book_time[i][j] = int(book_time[i][j][:2]) * \
                60 + int(book_time[i][j][3:])
    print(book_time)
    book_time.sort()
    room = [book_time[0]]
    print(book_time)
    for i in range(1, len(book_time)):
        for j in range(len(room)):
            if book_time[i][0] >= room[j][1] + 10:
                room[j] = book_time[i]
                break
        else:
            room.append(book_time[i])
    return len(room)
