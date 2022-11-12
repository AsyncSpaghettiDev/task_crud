import requests

BASE_URL = 'http://localhost:5000/tasks/'


def update_task(id, title, subtitle, body, active):
    task_data = {
        "title": title,
        "subtitle": subtitle,
        "body": body,
        "active": active
    }
    response = requests.put(f'{BASE_URL}{id}', json=task_data)
    if response.status_code == 204:
        print('Operation successful!')
    else:
        print('Something went wrong while trying to create a task!')


if __name__ == '__main__':
    print("Update a task by filling out the fields below:")
    id = int(input("ID of the task to update: "))
    title = input("Title: ")
    subtitle = input("Subtitle: ")
    body = input("Body: ")
    active_str = input("Active (T for true, anything for false): ")
    active = True if active_str == 'T' else False
    update_task(id, title, subtitle, body, active)
