import data_clean, data_deal, data_get

final_data = data_get.final_data("G0211807.334+", 24)
mean_values = data_clean.data_cleaning(final_data)
data_deal.data_predealing(mean_values)
