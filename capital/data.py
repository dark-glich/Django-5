from countryinfo import CountryInfo

def country_info(name):
    try:
        info = CountryInfo(name)
        capital = info.capital()
        currency = info.currencies()
        population = info.population()
        code = info.calling_codes()
        wiki = info.wiki()
        return [capital, currency, population, code, wiki]
    except KeyError:
        return ['No Data Found']

country_info('USAkfrkvrjvmfmvfmvrivrnr')

