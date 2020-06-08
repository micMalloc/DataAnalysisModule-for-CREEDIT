from openpyxl import load_workbook
from scipy import stats
import numpy
import pandas
import pandas_profiling


data = pandas.read_csv('/Users/heesu.lee/Desktop/Main/Creedit/kmong.csv')

print(data)

profile = pandas_profiling.ProfileReport(data)

profile.to_file('/Users/heesu.lee/Desktop/Main/Creedit/pr_report.html')

# def outliers_z_score(data):
#     threshold = 3
#     mean = numpy.mean(data)
#     std = numpy.std(data)
#     z_score = [(y - mean) / std for y in data]

#     return numpy.where(numpy.abs(z_score) <= threshold)

# load_wb = load_workbook('/Users/heesu.lee/Desktop/Main/Creedit/Crawling_Result.xlsx', data_only=True)
# load_ws = load_wb['Sheet1']

# # kmong = load_ws['C5':'C1284']
# otwojob = load_ws['D5':'D471']

# prices = []
# pre_prices = []

# for price in otwojob:
#     prices.append(price[0].value)

# # for i in outliers_z_score(prices)[0]:
# #     print(prices[i:i+1])

# for idx in outliers_z_score(prices)[0]:
#     pre_prices.append(prices[idx])

# print(numpy.mean(pre_prices))
