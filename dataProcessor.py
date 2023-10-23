import json
import os


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")


def get_ages(data):
    ages = []
    for person in data:
        ages.append(person['age'])
    return ages

# Modifique a função avgAgeCountry para que ela aceite uma função de transformação como segundo argumento. Esta função deve ser aplicada à idade antes de calcular a média (por exemplo, converter idade de anos para meses). Escreva testes para essa nova funcionalidade.
def avgAgeCountry(data, transform = lambda x: x):
    if len(data) == 0:
        return {}
    avgAges = {}
    for person in data:
        if 'age' not in person:
            raise Exception('Age not found')
        if 'country' not in person or person['country'] is None or person['country'] == '':
            raise Exception('Country not found')
        if person['country'] not in avgAges:
            avgAges[person['country']] = []
        avgAges[person['country']].append(transform(person['age']))
    for country in avgAges:
        media = sum(avgAges[country]) / len(avgAges[country])
        avgAges[country] = "%.2f" % media
    return avgAges


def qualPaisComMaiorMediaDeIdade(data):
    avgAges = avgAgeCountry(data)
    maiorMedia = 0
    pais = ''
    for country in avgAges:
        if float(avgAges[country]) > maiorMedia:
            maiorMedia = float(avgAges[country])
            pais = country
    return pais

def qualPaisComMenorMediaDeIdade(data):
    avgAges = avgAgeCountry(data)
    menorMedia = 100
    pais = ''
    for country in avgAges:
        if float(avgAges[country]) < menorMedia:
            menorMedia = float(avgAges[country])
            pais = country
    return pais


if __name__ == "__main__":
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "users.json")

    data = read_json_file(file_path)
    ages = get_ages(data)
    avgAges = avgAgeCountry(data)
    print(f"Average age: {sum(ages) / len(ages)}")
    print(f"Average age by country: {avgAges}")
