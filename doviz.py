import requests



api_key = "29f2b2f35b8db12a751e7ec497e2cf24" # yedek api_key : a98ef7f8958e7021680df392832d12c6
url = "http://data.fixer.io/api/latest?access_key=" + api_key

response = requests.get(url)

infos = response.json()

firstValue = infos["rates"]["USD"]
secondValue = infos["rates"]["TRY"]
thirdValue = infos["rates"]["EUR"]
def dolardovizfiyat():
    dolardoviz = secondValue / firstValue
    return dolardoviz
def eurdovizfiyat():
    eurdoviz = secondValue / thirdValue
    return eurdoviz

def eurdolar(): # 1 USD'nin EUR karşılığı
    eurdolardoviz = firstValue / thirdValue
    return eurdolardoviz

def dolareuro(): # 1 EUR'un USD karşılığı
    dolareurodoviz = thirdValue / firstValue
    return dolareurodoviz

