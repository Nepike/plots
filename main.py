import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(12, 6))

file_path = 'FILES/Eu152.xlsx'
df = pd.read_excel(file_path, skiprows=5)
channels = df['Channel'].values
counts = df['Counts'].values
plt.subplot(2, 3, 1)
plt.plot(channels, counts, 'b')
plt.title("Eu152")

file_path = 'FILES/Am241.xlsx'
df = pd.read_excel(file_path, skiprows=5)
channels = df['Channel'].values
counts = df['Counts'].values
plt.subplot(2, 3, 2)
plt.plot(channels, counts, 'r')
plt.title("Am241")

file_path = 'FILES/Na22.xlsx'
df = pd.read_excel(file_path, skiprows=5)
channels = df['Channel'].values
counts = df['Counts'].values
plt.subplot(2, 3, 3)
plt.plot(channels, counts, 'g')
plt.title("Na22")

file_path = 'FILES/Cs137.xlsx'
df = pd.read_excel(file_path, skiprows=5)
channels = df['Channel'].values
counts = df['Counts'].values
plt.subplot(2, 3, 4)
plt.plot(channels, counts, 'black')
plt.title("Cs137")

file_path = 'FILES/Co60.xlsx'
df = pd.read_excel(file_path, skiprows=5)
channels = df['Channel'].values[:-1200]
counts = df['Counts'].values[:-1200]
plt.subplot(2, 3, 5)
plt.plot(channels, counts, 'y')
plt.title("Co60")


plt.tight_layout()  # Автоматическое изменение расстояний между графиками
plt.show()
