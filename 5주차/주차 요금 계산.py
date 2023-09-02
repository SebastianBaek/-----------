# https://school.programmers.co.kr/learn/courses/30/lessons/92341
from math import ceil


def solution(fees, records):
    basic_time = fees[0]
    basic_fee = fees[1]
    interval = fees[2]
    extra_fee = fees[3]
    ans = []

    cars_time_dict = dict()
    records_dict = dict()
    for i in range(len(records)):
        record = records[i].split()

        hour_minute = record[0].split(":")
        car_num = record[1]
        minutes = int(hour_minute[0]) * 60 + int(hour_minute[1])
        if record[2] == "IN":
            records_dict[car_num] = minutes
        else:
            parking_time = minutes - records_dict[car_num]
            if car_num in cars_time_dict:
                cars_time_dict[car_num] += parking_time
            else:
                cars_time_dict[car_num] = parking_time
            del records_dict[car_num]

    day_end = 24 * 60 - 1
    for car_num, enter_time in list(records_dict.items()):
        if car_num in cars_time_dict:
            cars_time_dict[car_num] += day_end - enter_time
        else:
            cars_time_dict[car_num] = day_end - enter_time

    for car_num, entire_parking_time in list(cars_time_dict.items()):
        entire_parking_time -= basic_time
        if entire_parking_time <= 0:
            ans.append((car_num, basic_fee))
        else:
            ans.append(
                (car_num, basic_fee + ceil(entire_parking_time / interval) * extra_fee))

    ans.sort()
    return [fee for car_num, fee in ans]
