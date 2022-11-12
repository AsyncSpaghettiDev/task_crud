import requests

BASE_URL = 'http://localhost:5000/tasks/'


def delete_task(id):
    response = requests.delete(f'{BASE_URL}{id}')
    if response.status_code == 204:
        print('Task deleted!')
    else:
        print('Something went wrong while deleting the task, try it again!')


if __name__ == '__main__':
    print("Delete a task by entering the id:")
    id = int(input("ID of the task to delete: "))
    delete_task(id)
