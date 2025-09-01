import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
    for row in reader:
        print(row)

read_csv_file('ventas.csv')


countries_list = [
	{
		'name': 'Costa Rica',
		'capital': 'San José',
		'currency': 'Colón',
		'area_km2': '51,100',
	},
	{
		'name': 'Colombia',
		'capital': 'Bogotá',
		'currency': 'Peso Colombiano',
		'area_km2': '1,141,748',
	},
	{
		'name': 'México',
		'capital': 'Ciudad de México',
		'currency': 'Peso Mexicano',
		'area_km2': '1,972,550',
	},
]

country_headers = (
	'name',
	'capital',
	'currency',
	'area_km2',
)

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

write_csv_file('countries.csv', countries_list, country_headers)



countries_list = [
	{
		'name': 'Costa Rica',
		'capital': 'San José',
		'currency': 'Colón',
		'area_km2': '51,100',
	},
	{
		'name': 'Colombia',
		'capital': 'Bogotá',
		'currency': 'Peso Colombiano',
		'area_km2': '1,141,748',
	},
	{
		'name': 'México',
		'capital': 'Ciudad de México',
		'currency': 'Peso Mexicano',
		'area_km2': '1,972,550',
	},
]

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

write_csv_file('countries.csv', countries_list, countries_list[0].keys())