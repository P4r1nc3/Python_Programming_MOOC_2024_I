# Write your solution here
def read_file(filename: str):
    file_lines = []
    with open(filename) as file:
        for line in file:
            line = line.replace('\n', '')
            file_lines.append(line)
    return file_lines

def create_recipes_from_file(filename: str):
    recipes = []
    file_lines = read_file(filename)
    total_recipes = file_lines.count('')+1
    start_index = 0
    for i in range(total_recipes):
        dict = {}
        dict['name'] = file_lines[start_index]
        dict['prep_time'] = file_lines[start_index+1]
        try:
            end_index = file_lines.index('', start_index)
        except:
            end_index = len(file_lines)
        dict['ingredients'] = file_lines[start_index+2:end_index]
        start_index = end_index+1
        recipes.append(dict)
    return recipes

def search_by_name(filename: str, word: str):
    recipes = create_recipes_from_file(filename)
    found_recipes = []
    for i in range(len(recipes)):
        name = recipes[i]['name']
        if word.lower() in name.lower():
            found_recipes.append(name)

    return found_recipes

def search_by_time(filename: str, prep_time: int):
    recipes = create_recipes_from_file(filename)
    found_recipes = []
    for i in range(len(recipes)):
        time = int(recipes[i]['prep_time'])
        if time <= prep_time:
            recipe = recipes[i]['name'] + ', ' + 'preparation time ' + str(time) + ' min'
            found_recipes.append(recipe)
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipes = create_recipes_from_file(filename)
    found_recipes = []
    for i in range(len(recipes)):
        for ingr in recipes[i]['ingredients']:
            if ingr == ingredient:
                time = int(recipes[i]['prep_time'])
                recipe = recipes[i]['name'] + ', ' + 'preparation time ' + str(time) + ' min'
                found_recipes.append(recipe)
    return found_recipes