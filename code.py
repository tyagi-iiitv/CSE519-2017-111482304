# # Lines after 2973782 were removed because of no data.
# # Read the fields from the csv
# import pandas as pd
# data = pd.read_csv('data/properties_2016.csv', usecols=['parcelid',
#                                                         'bedroomcnt', # Float64
#                                                         'buildingqualitytypeid', # Float64
#                                                         'calculatedfinishedsquarefeet', #Float64
#                                                         'numberofstories', #Float64
#                                                         'lotsizesquarefeet', #Float64
#                                                         'taxamount', #Float64
#                                                         ], index_col='parcelid')
# logerror_data = pd.read_csv('data/train_2016_v2.csv', usecols=['parcelid','logerror'], index_col='parcelid')
# data = data.join(logerror_data, how='outer') # takes the union of the indices
# # data = data.dropna(axis=0, how='any')
# # data.drop('parcelid',axis=1)
# data = data.rename(index=str, columns={'bedroomcnt':'BedCnt','buildingqualitytypeid':'BldnQlty','calculatedfinishedsquarefeet':'sqFeet','numberofstories':'Stories','lotsizesquarefeet':'lotsize','taxamount':'tax'})
#
# # print data
#
# # import numpy as np;
# # import pandas as pd
# # import seaborn.apionly as sns
# # import matplotlib.pyplot as plt
# #
# # # Generate a random dataset
# #
# # # Compute the correlation matrix
# # corr = data.corr()
# # # print(corr)
# # # Generate a mask for the upper triangle
# # mask = np.zeros_like(corr, dtype=np.bool) # returns an array of zeros of the same shape and size as corr mat
# # mask[np.triu_indices_from(mask)] = True # makes the upper triangle of mask as 1
# #
# # # Set up the matplotlib figure
# # fig, ax = plt.subplots()
# #
# # # Draw the heatmap with the mask and correct aspect ratio
# # vmax = np.abs(corr.values[~mask]).max()
# # sns.heatmap(corr, mask=mask, cmap=plt.cm.PuOr, vmin=-vmax, vmax=vmax,
# #             square=True, linecolor="lightgray", linewidths=1, ax=ax) # Masks the upper triangle of the heatmap
# # for i in range(len(corr)):
# #     ax.text(i+0.5,i+0.5, corr.columns[i],
# #             ha="center", va="center", rotation=45)
# #     for j in range(i+1, len(corr)):
# #         s = "{:.3f}".format(corr.values[i,j])
# #         ax.text(j+0.5,i+0.5,s,
# #             ha="center", va="center")
# # ax.axis("off")
# # plt.show()
#
#
#
# import numpy as np
# # # Removing the NAN values from bedroomcnt
# # bedroom_cnt = data['bedroomcnt'][numpy.logical_not(numpy.isnan(data['bedroomcnt']))]
# # # Similarly removing NAN values for each of the properties
# # building_quality_typeid = data['buildingqualitytypeid'][numpy.logical_not(numpy.isnan(data['buildingqualitytypeid']))]
# # calculated_finished_square_feet = data['calculatedfinishedsquarefeet'][numpy.logical_not(numpy.isnan(data['calculatedfinishedsquarefeet']))]
# # number_of_stories = data['numberofstories'][numpy.logical_not(numpy.isnan(data['numberofstories']))]
# # lot_size_square_feet = data['lotsizesquarefeet'][numpy.logical_not(numpy.isnan(data['lotsizesquarefeet']))]
# # tax_amount = data['taxamount'][numpy.logical_not(numpy.isnan(data['taxamount']))]
# import matplotlib.pyplot as plt
# data = data.reset_index()
# sqFeet = data['sqFeet'][np.logical_not(np.isnan(data['sqFeet']))]
# sqFeet = sqFeet[sqFeet != 0]
# plt.plot(sqFeet,'o', ms=1)
# plt.xlabel('Houses')
# plt.ylabel('Total square feet')
# # print sqFeet
# plt.show() # Bedroom count ranges from 0 to 20.
#
# # Calculating the mean values of each of the properties to fill up in place of NAN values.
# # mean_bedroom_cnt = numpy.mean(bedroom_cnt)
# # mean_building_quality_typeid = numpy.mean(building_quality_typeid)
# # mean_calculated_finished_square_feet = numpy.mean(calculated_finished_square_feet)
# # mean_number_of_stories = numpy.mean(number_of_stories)
# # mean_lot_size_square_feet = numpy.mean(lot_size_square_feet)
# # mean_tax_amount = numpy.mean(tax_amount)
# # Replacing all the NAN values with the means for all the properties
# # nans = numpy.isnan(data['bedroomcnt'])
# # data['bedroomcnt'][nans] = mean_bedroom_cnt
# # nans = numpy.isnan(data['buildingqualitytypeid'])
# # data['buildingqualitytypeid'][nans] = mean_building_quality_typeid

import pandas as pd
import numpy as np
import seaborn.apionly as sns
import matplotlib.pyplot as plt
county_arch = pd.read_csv('data/properties_2016.csv', usecols=['regionidcounty','architecturalstyletypeid', 'regionidcity'])
print county_arch
# county_arch['regionidcounty'].value_counts(normalize=False, sort=True, dropna=True).plot(kind='pie')
# plt.axis('equal')
# plt.show()
# plt.pie(county_unique_count, labels=county_unique_id)
# plt.axis('equal')
# plt.show()