print("Hola")
import random
from datetime import datetime, timedelta
import pandas as pd

CEDULA = input("Ingresa tu número de cédula: ")
random.seed(int(CEDULA))

N = 10_000
base_date = datetime(2026, 1, 1)

machines = pd.DataFrame({
    "machine_id": range(1, 51),
    "line_id": [random.randint(1, 10) for _ in range(50)],
    "machine_type": [random.choice(["CNC", "Ensamblaje", "Empaque", "Corte"]) for _ in range(50)],
    "install_date": [base_date - timedelta(days=random.randint(0, 3000)) for _ in range(50)],
})

shifts = pd.DataFrame({
    "shift_id": [1, 2, 3],
    "start_time": ["06:00", "14:00", "22:00"],
    "end_time": ["14:00", "22:00", "06:00"],
    "supervisor": [f"Supervisor_{i}" for i in range(1, 4)],
})

orders = []
for order_id in range(1, N + 1):
    machine_id = random.choice(machines["machine_id"])
    line_id = machines.loc[machines.machine_id == machine_id, "line_id"].values[0]
    start = base_date + timedelta(minutes=random.randint(0, 60 * 24 * 180))
    end = start + timedelta(minutes=random.randint(30, 240))
    units = random.randint(50, 500)
    defective = int(units * random.uniform(0, 0.08))
    orders.append({
        "order_id": order_id, "line_id": line_id, "machine_id": machine_id,
        "product_id": random.randint(1, 20), "start_time": start, "end_time": end,
        "units_produced": units, "units_defective": defective,
        "shift_id": random.choice(shifts["shift_id"]),
    })
orders_df = pd.DataFrame(orders)

downtime = []
for event_id in range(1, N + 1):
    start = base_date + timedelta(minutes=random.randint(0, 60 * 24 * 180))
    end = start + timedelta(minutes=random.randint(5, 180))
    downtime.append({
        "event_id": event_id,
        "machine_id": random.choice(machines["machine_id"]),
        "start_time": start, "end_time": end,
        "type": random.choice(["planned", "unplanned"]),
        "reason_code": random.choice(["MEC-01", "MEC-02", "ELEC-01", "CAL-01", "MAT-01"]),
        "order_id": random.choice(orders_df["order_id"]) if random.random() > 0.3 else None,
    })
downtime_df = pd.DataFrame(downtime)

machines.to_csv("machines.csv", index=False)
shifts.to_csv("shifts.csv", index=False)
orders_df.to_csv("production_orders.csv", index=False)
downtime_df.to_csv("downtime_events.csv", index=False)
