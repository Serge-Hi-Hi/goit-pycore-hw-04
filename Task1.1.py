def total_salary(path:str):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='UTF-8') as file:

            for line in file:
                name, salary = line.split(',')
                total = total + int(salary)
                count += 1

        average = total / count if count > 0 else 0

        return total, average


    except Exception as e :
        print('Файл не знайдено : {e}')

        return 0, 0

total, average = total_salary('path/to/salary_file.txt')

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")
