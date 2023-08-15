import pandas as pd

df = pd.read_csv("nba.csv")

# # print(df.head())

# # for i in df:
# #     print(i)

# for nombre in df.nombre:
#     print(nombre)

# #me muestra todos los registros menos los repetidos, de ese campo "nombre"
# #print(df.nombre.unique())


# #condicionales dentro del df en la columna nombre == jordan, o donde pos > 3
# print(df[df.nombre=="jordan"])
# print(df[df.pos>3])

# #elimnar datos o columnas

df1 = pd.read_csv("nba.csv")

#aca elimina toda la columna posicion y lo guarda en el nuevo dataframe "df2"
df2 = df1.drop("pos",axis=1)
print(df2)

#renombrar columnas
df2 = df2.rename(columns={"nombre":"jugador"})
#renombrar campos especificos, en este caso estoy eliminando a todos los "malone"
df2=df2[df2.jugador!="malone"]

#almacenar un nuevo df

df2.to_csv("nba2.csv")


#MATPLOTLIB

import matplotlib.pyplot as plt

x = df1.nombre
y = df1.puntos
size = (10,5)

plt.figure(figsize=size)
plt.bar(x,y)
plt.show()