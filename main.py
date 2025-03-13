from data_loader import save_data
import pandas as pd
from shot_analysis import shot_efficiency
from visualizations import plot_shot_efficiency

df = pd.read_csv('match_data.csv')


print("Columns in DataFrame:", df.columns)


shot_efficiency(df)


save_data()


plot_shot_efficiency(df)
