def get_cats_info(path: str) -> list:
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')

                cat = {
                    'id': cat_id,
                    'name':cat_name,
                    'age': cat_age,
                }

                cats_info.append(cat)

        return cats_info



    except Exception as e:
        print(f'Помилка читання файлу: {e}' )

        return []

cats_info = get_cats_info('path/to/cats_file.txt')
print(cats_info)
