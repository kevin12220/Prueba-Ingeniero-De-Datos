import psycopg2   
import csv

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'project'
DB_USER = 'postgres'
DB_PASSWORD = '12345'
DB_PORT = '5432'

# Function to connect to PostgreSQL
def connect_to_db():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

# Main function to ingest data
def ingest_data():
    # Connect to PostgreSQL
    conn = connect_to_db()
    cur = conn.cursor()

    # Open the CSV file
    with open(r'C:\Users\valen13\Downloads\Prueba Tecnica\Api\src\data.csv', 'r') as file:
        data_reader = csv.DictReader(file, delimiter=";")
        data_reader.fieldnames = [
           campo.strip()
           for campo in data_reader.fieldnames
        ]

        # Insert each row into the table
        for row in data_reader:
            print(row)
            print(len(row))
            cur.execute("INSERT INTO users (id, nombre, correo, telefono) VALUES (%s, %s, %s, %s)""",
                        
                          (
                             int(row["id"]),
                             row["nombre"],
                             row["correo"],
                             row["telefono"]
                          )
                        )
    # Commit and close the connection
    conn.commit()
    cur.close()
    conn.close()
    print("Data ingested successfully")

if __name__ == "__main__":
    ingest_data()