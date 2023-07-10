import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv(path)
    chart_type = input("which type of graph do you want? Bar chart or Pie chart: ")
    chart_type = chart_type.capitalize()

    if chart_type == "Bar chart" or chart_type == "Bar":
        country = input("Type Country: ")
        country = country.title()

        result = utils.population_by_country(data, country)

        if len(result) > 0:
            country = result[0]
            labels, values = utils.get_population(country)
            print(labels, values)
            charts.generate_bar_chart(labels, values)

    elif chart_type == "Pie chart" or chart_type == "Pie":
        continent = input("Type continent: ")
        continent = continent.title()
        data = list(filter(lambda item: item["Continent"] == continent, data))

        countries, percentages = utils.get_percentages(data)
        charts.generate_pie_chart(countries, percentages)   

    else:
        print("Please write a correct option")

if __name__ == "__main__":
    run()
