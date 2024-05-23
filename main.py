import requests


def get_url(food: str) -> str:
    food = food.lower()
    url = "https://api.spoonacular.com/recipes/complexSearch?query="
    url += food
    return url


def get_response(url: str) -> requests.Response:
    resp = requests.get(url, params={'apiKey': '76f5d9a23a58426aa9028a708ec23d0e'})
    return resp


def get_n_print_data(resp: requests.Response) -> dict:
    recp_ids= {}
    for i, food in enumerate(resp.json()['results']):
        print(f"Название блюда №{i+1}: {food['title']}\nКартинка: {food['image']}\n")
        recp_ids[f'{i+1}'] = food['id']
    return recp_ids


cin = input

r = get_response(get_url(cin('Введите название искомых блюд: ')))
if r.status_code == 200:
    print('')
recepies = get_n_print_data(r)
id = recepies[cin('Введите номер блюда, рецепт которого вам нужен: ')]
print('WIP')
recept = get_response(f"https://api.spoonacular.com/recipes/{id}/information").json()