def convert_units():
    cm = float(input("Введите длину в сантиметрах: "))
    meters = float(input("Введите длину в метрах: "))
    
    # Перевод в английскую систему
    cm_to_inches = cm / 2.54
    meters_to_feet = meters / 0.3048

    print(f"Длина в дюймах: {cm_to_inches} in")
    print(f"Длина в футах: {meters_to_feet} ft")

convert_units()
