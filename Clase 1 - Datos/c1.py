import pandas as pd
import numpy as np
import matplotlib

# ds=[2,3,4,5,4,5,5,3,3,2]

# largo=len(ds)

# total = 0

# for i in ds:
#     total=total+i

# print(largo)
# print(total)

# print(f"La media del dataset es de: {total/largo}")

# ultimo = len(ds)-1
# print(ultimo)

# #usando pandas 

df = pd.read_csv("animales.csv")

print(df)


for i in df:
    print(i)

print(df.head())


#para recorrer por columna


print(df[df['animal'] == "perro"])