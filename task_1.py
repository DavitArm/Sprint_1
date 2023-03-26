times = '1h 45m,360s,25m,30m 120s,2h 60s'
count_minutes = 0

for time in times.split(','):
    for time_part in time.split():
        if 'h' in time_part[-1]:
            count_minutes += int(time_part[:-1]) * 60
        elif 'm' in time_part[-1]:
            count_minutes += int(time_part[:-1])
        elif 's' in time_part[-1]:
            count_minutes += int(time_part[:-1]) // 60

print(count_minutes)
