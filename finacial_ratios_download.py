import numpy as np
import pandas as pd
import requests
import json


def financialratios(company, is_oneyearonly, api_key):
    if type(company) == list:
            if is_oneyearonly:
                alldf = {}
                for x in company:
                    print(x)
                    fr = requests.get(
                        f"https://financialmodelingprep.com/api/v3/financial-ratios/{x}?apikey={api_key}")
                    fr = fr.json()
                    fr = fr['ratios']
                    valuation = fr[0]['investmentValuationRatios']
                    profitability = fr[0]['profitabilityIndicatorRatios']
                    operating = fr[0]['operatingPerformanceRatios']
                    liquidity = fr[0]['liquidityMeasurementRatios']
                    debt = fr[0]['debtRatios']
                    valuation = pd.DataFrame(valuation.items(), columns=['Ratio', company])
                    print(valuation)
                    profitability = pd.DataFrame(list(profitability.items()), columns=['Ratio', company])
                    operating = pd.DataFrame(list(operating.items()), columns=['Ratio', company])
                    liquidity = pd.DataFrame(list(liquidity.items()), columns=['Ratio', company])
                    debt = pd.DataFrame(list(debt.items()), columns=['Ratio', company])
                    frames = [valuation, profitability, operating, liquidity, debt]
                    result = pd.concat(frames)
                    alldf[x] = result
                return alldf
            else:
                alldf = {}
                for x in company:
                    i = 0
                    fr = requests.get(
                        f"https://financialmodelingprep.com/api/v3/financial-ratios/{x}?apikey={api_key}")
                    fr = fr.json()
                    fr = fr["ratios"]
                    final = pd.DataFrame(columns=["Ratio"])
                    for xx in fr:
                        Date = fr[i]["date"]
                        valuation = fr[i]['investmentValuationRatios']
                        profitability = fr[i]['profitabilityIndicatorRatios']
                        operating = fr[i]['operatingPerformanceRatios']
                        liquidity = fr[i]['liquidityMeasurementRatios']
                        debt = fr[i]['debtRatios']
                        valuation = pd.DataFrame(list(valuation.items()), columns=['Ratio', Date])
                        profitability = pd.DataFrame(list(profitability.items()), columns=['Ratio', Date])
                        operating = pd.DataFrame(list(operating.items()), columns=['Ratio', Date])
                        liquidity = pd.DataFrame(list(liquidity.items()), columns=['Ratio', Date])
                        debt = pd.DataFrame(list(debt.items()), columns=['Ratio', Date])
                        frames = [valuation, profitability, operating, liquidity, debt]
                        result = pd.concat(frames)
                        if i == 0:
                            final = result
                        else:
                            result = result[str(Date)]
                            final = pd.concat([final, result], axis=1)
                        i = i + 1
                    final = final.drop_duplicates()
                    alldf[f"{x}"] = final
                return alldf
    else:
        i = 0
        fr = requests.get(f"https://financialmodelingprep.com/api/v3/financial-ratios/{company}?apikey={api_key}")
        fr = fr.json()
        fr = fr["ratios"]
        if is_oneyearonly:
            valuation = fr[0]['investmentValuationRatios']
            profitability = fr[0]['profitabilityIndicatorRatios']
            operating = fr[0]['operatingPerformanceRatios']
            liquidity = fr[0]['liquidityMeasurementRatios']
            debt = fr[0]['debtRatios']
            valuation = pd.DataFrame(list(valuation.items()), columns=['Ratio', company])
            profitability = pd.DataFrame(list(profitability.items()), columns=['Ratio', company])
            operating = pd.DataFrame(list(operating.items()), columns=['Ratio', company])
            liquidity = pd.DataFrame(list(liquidity.items()), columns=['Ratio', company])
            debt = pd.DataFrame(list(debt.items()), columns=['Ratio', company])
            frames = [valuation, profitability, operating, liquidity, debt]
            result = pd.concat(frames)
            result = result.drop_duplicates()
            return result
        else:
            fr = fr["ratios"]
            final = pd.DataFrame(columns=["Ratio"])
            for x in fr:
                Date = fr[i]["date"]
                valuation = fr[i]['investmentValuationRatios']
                profitability = fr[i]['profitabilityIndicatorRatios']
                operating = fr[i]['operatingPerformanceRatios']
                liquidity = fr[i]['liquidityMeasurementRatios']
                debt = fr[i]['debtRatios']
                valuation = pd.DataFrame(list(valuation.items()), columns=['Ratio', Date])
                profitability = pd.DataFrame(list(profitability.items()), columns=['Ratio', Date])
                operating = pd.DataFrame(list(operating.items()), columns=['Ratio', Date])
                liquidity = pd.DataFrame(list(liquidity.items()), columns=['Ratio', Date])
                debt = pd.DataFrame(list(debt.items()), columns=['Ratio', Date])
                frames = [valuation, profitability, operating, liquidity, debt]
                result = pd.concat(frames)
                if i == 0:
                    final = result
                else:
                    result = result[str(Date)]
                    final = pd.concat([final, result], axis=1)
                i = i + 1
            final = final.drop_duplicates()
            return final


def peerfinancialratios(main_company, api_key):
    i = 0
    for item in main_company:
        y = financialratios(item, True, api_key)
        if i == 0:
            x = y
            i = i + 1
        else:
            x = x.merge(y, on='Ratio')
    x.to_csv("ratios_financieros_comparativo.csv")
    return x

def transform (data, companies):
    if type(companies) == list:
        for x in companies:
            xx = data[f"{x}"]
            xx.to_csv(f"FinancialRatios{x}.csv")
    else:
        data.to_csv(f"FinancialRatios{companies}.csv")