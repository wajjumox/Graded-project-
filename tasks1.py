
seltos_units = 300
sonet_units = 450
total_units = seltos_units + sonet_units  # Total units sold
difference_units = abs(seltos_units - sonet_units)  # Absolute difference
ratio_units = seltos_units / sonet_units  # Ratio of Seltos to Sonet sales
print(f"Total units sold: {total_units}")
print(f"Difference in units sold: {difference_units}")
print(f"Ratio of units sold (Seltos to Sonet): {ratio_units:.2f}")