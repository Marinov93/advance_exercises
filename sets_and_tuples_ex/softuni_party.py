# 2 types of guests -> Regular and VIP ( reservation lists)

number_guests = int(input())

regular_guest = set()
vip_guest = set()

for i in range(number_guests):
    reservation_codes = input()
    if reservation_codes[0].isdigit():
        vip_guest.add(reservation_codes)
    else:
        regular_guest.add(reservation_codes)

command = input()
while command != 'END':
    if command[0].isdigit():
        if command in vip_guest:
            vip_guest.remove(command)
    else:
        if command in regular_guest:
            regular_guest.remove(command)
    command = input()

vip_guest_sorted = sorted(vip_guest)
regular_guest_sorted = sorted(regular_guest)

print(len(vip_guest) + len(regular_guest))
print(*vip_guest_sorted, sep='\n')
print(*regular_guest_sorted, sep='\n')
