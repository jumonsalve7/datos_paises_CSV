import read_csv
import charts
import utils

def run():
    # Leer los datos del archivo CSV
    data = read_csv.read_csv("data.csv")

    data = list(filter(lambda item: item["Continent"] == "South America", data))
    
    # Obtener los nombres de los países y los porcentajes de población mundial
    countries = list(map(lambda x: x["Country/Territory"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    
    # Generar gráfico de pastel con los datos de Sudamérica
    charts.generate_pie_chart(countries, percentages)

    # Solicitar el país al usuario
    country_name = input("Type your country => ").strip()
    print("País ingresado:", country_name)
    
    # Buscar datos del país especificado
    result = utils.population_by_country(data, country_name)


    if len(result) > 0:
        country_data = result[0]
        print("Datos del país:", country_data)
        labels, values = utils.get_population(country_data)
        
        # Generar gráfico de barras con los datos del país
        charts.generate_bar_chart(country_name, labels, values)

if __name__ == "__main__":
    run()