import requests

BASE_URL = "http://127.0.0.1:5000"


def test_get_tasks():
    print("\n📌 Récupérer toutes les tâches")
    r = requests.get(f"{BASE_URL}/task")
    print(r.status_code, r.json())


def test_create_task():
    print("\n📌 Créer une nouvelle tâche")
    payload = {
        "id": 1,
        "title": "Première tâche",
        "description": "Description de la première tâche",
    }
    r = requests.post(f"{BASE_URL}/task", json=payload)
    print(r.status_code, r.json())


def test_update_task():
    print("\n📌 Mettre à jour la tâche (id=1)")
    r = requests.put(
        f"{BASE_URL}/task/1",
        json={
            "title": "Tâche modifiée",
            "description": "Nouvelle description",
            "completed": True,
        },
    )
    print(r.status_code, r.text)  # utilise .text pour voir la vraie réponse brute
    try:
        print("JSON:", r.json())
    except:
        print("⚠️ Pas de JSON valide dans la réponse")


def test_delete_task():
    print("\n📌 Supprimer la tâche (id=1)")
    r = requests.delete(f"{BASE_URL}/task/1")
    print(r.status_code, r.json())


if __name__ == "__main__":
    test_get_tasks()
    test_create_task()
    test_get_tasks()
    test_update_task()
    test_get_tasks()
    test_delete_task()
    test_get_tasks()
