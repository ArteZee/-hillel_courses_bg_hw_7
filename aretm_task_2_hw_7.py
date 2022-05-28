print("Введите порядковый номер месяца " )
month = int(input())

def season(month):
    if month == 12 or month == 1 or month == 2:
        return "winter"
    elif 3 <= month <= 5:
        return "spring"
    elif 6 <= month <= 8:
        return "summer"
    elif 9 <= month <= 11:
        return "autumn"

print(season(month))
