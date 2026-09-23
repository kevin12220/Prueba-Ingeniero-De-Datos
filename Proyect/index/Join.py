import pandas as pd

production_orders = pd.read_csv(r"C:\Users\valen13\Downloads\Prueba Tecnica\Proyect\src\production_orders.csv")
shift = pd.read_csv(r"C:\Users\valen13\Downloads\Prueba Tecnica\Proyect\src\shifts.csv")


df = pd.merge(
production_orders,
shift,
on="shift_id",
how="inner"
)


df["unidades_optimas"] = (
df["units_produced"] -
df["units_defective"]
)

print(df[[
"order_id",
"machine_id",
"shift_id",
"supervisor",
"units_produced",
"units_defective",
"unidades_optimas"
]])


resultado = df[
[
"order_id",
"machine_id",
"shift_id",
"supervisor",
"units_produced",
"units_defective",
"unidades_optimas",
]
]
resultado.to_csv(
r"C:\Users\valen13\Downloads\Prueba Tecnica\Proyect\src\unidades_optimas.csv",
index=False,
encoding="utf-8"
)
print("Archivo CSV generado correctamente")