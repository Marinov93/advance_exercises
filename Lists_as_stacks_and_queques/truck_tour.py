# from collections import deque
# #input
# pumps_data = deque([[int(x) for x in input().split()] for i in range(int(input()))])
#
# pumps_data_copy = pumps_data.copy()
# gas = 0
# index = 0
#
# while pumps_data_copy:
#     benz, distance = pumps_data_copy.popleft()
#
#     gas += benz
#
#     if gas >= distance:
#         gas -= distance
#     else:
#         pumps_data.rotate(-1)
#         pumps_data_copy = pumps_data.copy()
#         index += 1
#         gas = 0
# print(index)
from collections import deque

pumps_number = int(input())
pumps = deque()

for _ in range(pumps_number):
    fuel, distance = input().split()
    pumps.append([int(fuel), int(distance)])

inx = 0
stops = 0

while stops < pumps_number:
    fuel = 0
    for i in range(pumps_number):
        fuel += pumps[i][0]
        distance = pumps[i][1]
        if fuel < distance:
            pumps.rotate(-1)
            inx += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(inx)