import os 
import pandas as pd
import dirs as dr

os.system('cls')
path_1 = dr.path_1
path_2 = dr.path_2

list1 = os.listdir(path_1)
list2 = os.listdir(path_2)
borrar = []

for item in list1:
    if item in list2:
        borrar.append(item)

df = pd.DataFrame()
df['Nombre'] = borrar

df.to_csv(f"{path_2}/borrados.csv", index=0, header=True, encoding='utf-8-sig')
print(df)


for pista in borrar:
    os.remove(path_2+pista)