def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [int(line.split(",")[1]) for line in file if line.strip()]
    except (OSError, ValueError, IndexError):
        print(f"Файл {path} не знайдено або він пошкоджений")
        return 0, 0

    total = sum(salaries)
    return total, (total / len(salaries) if salaries else 0)


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




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

total, average = total_salary('path/to/cats_file.txt')

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")
