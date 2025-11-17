total_minutes = int(input())

hours = total_minutes // 60
minutes_left = total_minutes % 60

print(f"{total_minutes} мин - это {hours} час {minutes_left} минут")
