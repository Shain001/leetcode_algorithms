import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib import ticker
from matplotlib import rcParams
from datetime import timedelta
import numpy as np

df1 = pd.read_csv('E:\\MinorThesis\\exp\\v2\\fig0\\exp-compare-two-models-fuel-when-same-weight-0per.txt', sep=" ", header = None)

df2 = pd.read_csv('E:\\MinorThesis\\exp\\v2\\fig0\\exp-compare-two-models-fuel-when-same-weight-70per.txt', sep=" ", header = None)
print(df1)


df_60 = df1[(df1[0] > 15) & (df1[0] < 25)]
df_80 = df1[(df1[0] > 35) & (df1[0] < 45)]
df_100 = df1[(df1[0] > 55) & (df1[0] < 65)]
df_120 = df1[(df1[0] > 75) & (df1[0] < 85)]
df_140 = df1[(df1[0] > 95) & (df1[0] < 105)]

# 60
fuel_vt_20 = df_60[2].mean()
fuel_avg_20 = df_60[3].mean()

fuel_vt_40 = df_80[2].mean()
fuel_avg_40 = df_80[3].mean()

fuel_vt_60 = df_100[2].mean()
fuel_avg_60 = df_100[3].mean()

fuel_vt_80 = df_120[2].mean()
fuel_avg_80 = df_120[3].mean()

fuel_vt_100 = df_140[2].mean()
fuel_avg_100 = df_140[3].mean()

##
df_60_2 = df2[(df1[0] > 15) & (df1[0] < 25)]
df_80_2 = df2[(df1[0] > 35) & (df1[0] < 45)]
df_100_2 = df2[(df1[0] > 55) & (df1[0] < 65)]
df_120_2 = df2[(df1[0] > 75) & (df1[0] < 85)]
df_140_2 = df2[(df1[0] > 95) & (df1[0] < 105)]

# 60
fuel_vt_202 = df_60_2[2].mean()
fuel_avg_202 = df_60_2[3].mean()

fuel_vt_402 = df_80_2[2].mean()
fuel_avg_402 = df_80_2[3].mean()

fuel_vt_602 = df_100_2[2].mean()
fuel_avg_602 = df_100_2[3].mean()

fuel_vt_802 = df_120_2[2].mean()
fuel_avg_802 = df_120_2[3].mean()

fuel_vt_1002 = df_140_2[2].mean()
fuel_avg_1002 = df_140_2[3].mean()

x_axis = [20, 40, 60, 80, 100]

y1 = [fuel_vt_20, fuel_vt_40, fuel_vt_60, fuel_vt_80, fuel_vt_100]
y2 = [fuel_avg_20, fuel_avg_40, fuel_avg_60, fuel_avg_80, fuel_avg_100]

y3 = [fuel_vt_202, fuel_vt_402, fuel_vt_602, fuel_vt_802, fuel_vt_1002]
y4 = [fuel_avg_202, fuel_avg_402, fuel_avg_602, fuel_avg_802, fuel_avg_1002]

plt.rcParams.update({'font.size': 14})
plt.subplot(1,2,1)
plt.plot(x_axis, y1, marker='o', label="VT-CPFM Model")
plt.plot(x_axis, y2, marker='s', label="Mesoscopic Model")

plt.xticks(x_axis, fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("Travel Distance (KM)", fontsize=20)
plt.ylabel("Fuel Consumption (L)", fontsize=20)
plt.ylim(ymin=0)
plt.legend()
plt.title("Fuel Consumption Comparison (0% Traffic Signal)", fontsize=20)

plt.subplot(1,2,2)
plt.plot(x_axis, y3, marker='o', label="VT-CPFM Model")
plt.plot(x_axis, y4, marker='s', label="Mesoscopic Model")

plt.xticks(x_axis)
plt.yticks(fontsize=20)
plt.xlabel("Travel Distance (KM)", fontsize=20)
plt.ylabel("Fuel Consumption (L)", fontsize=20)
plt.ylim(ymin=0)
plt.legend()
plt.title("Fuel Consumption Comparison (70% Traffic Signal)", fontsize=20)

plt.suptitle('Experiment Result - Accuracy Comparison for VT-CPFM and Mesoscopic Model', fontsize=25)
plt.show()



















