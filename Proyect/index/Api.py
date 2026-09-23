import csv
import requests
import psycopg2

url = "https://jsonplaceholder.typicode.com/users/1/posts"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()

    print(f"Total de registros: {len(users)}")

    for post in users[:6]:
        print(f"ID: {post['id']}")
        print(f"Título: {post['title']}")
        print(f"Contenido: {post['body']}")
        print("-" * 80)
else:
    print("Error:", response.status_code)


