import requests

URL_BASE = "https://jsonplaceholder.typicode.com"

HEADERS = {
    "Content-Type": "application/json; charset=UTF-8"
}

def get_users():
    response = requests.get(f"{URL_BASE}/users", headers=HEADERS)
    if response.status_code == 200:
        print("Usuarios obtenidos correctamente.")
    else:
        print(f"Error GET /users: {response.status_code}")
    return response


def get_all_posts():
    response = requests.get(f"{URL_BASE}/posts", headers=HEADERS)
    if response.status_code == 200:
        print("Posts obtenidos correctamente.")
    else:
        print(f"Error GET /posts: {response.status_code}")
    return response

def create_post(title, body, user_id):
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(f"{URL_BASE}/posts", headers=HEADERS, json=payload)
    if response.status_code == 201:
        print("Post creado exitosamente:", response.json())
    else:
        print(f"Error POST /posts: {response.status_code}")
    return response

def update_post(post_id, title, body, user_id):
    payload = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.put(f"{URL_BASE}/posts/{post_id}", headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"Post {post_id} actualizado exitosamente:", response.json())
    else:
        print(f"Error PUT /posts/{post_id}: {response.status_code}")
    return response

def delete_post(post_id):
    response = requests.delete(f"{URL_BASE}/posts/{post_id}", headers=HEADERS)
    if response.status_code == 200:
        print(f"Post {post_id} eliminado correctamente")
    else:
        print(f"Error DELETE /posts/{post_id}: {response.status_code}")
    return response