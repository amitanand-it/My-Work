

import plotly.express as px
import pandas as pd



df = pd.read_csv('/Users/tradeindia/Downloads/LearnerSummary_31Dec2021-01Jun2022.csv')

y = ["Days Logged In","Hours Viewed","Course Views","Course Completions","Video Views","Video Completions"]

chart = px.bar(df, x='Email' , y = y,  barmode="group")
chart.show()





