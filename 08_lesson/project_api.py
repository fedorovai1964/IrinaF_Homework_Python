import  requests
from config import token


class ProjectApi():
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
    # метод создания проекта
    def post_create_project(self,name):
        payload = {
            "title": name
        }
        resp = requests.request(
            "POST", self.url, json=payload, headers=self.headers)
        return resp

    # метод просмотра проекта
    def get_project(self,id):
        resp = requests.request(
            "GET", self.url + f"/{id}", headers=self.headers)
        return resp

    # метод изменения проекта
    def put_сhange_project(self, id, name):
        payload = {
            "title": name
        }
        resp = requests.request(
            "PUT", self.url + f'/{id}', json=payload, headers=self.headers)
        return resp

    # метод очистки данных после теста
    def delete_project(self, id): # "deleted": True,
        payload = {
            "deleted": True
        }
        requests.request(
            "PUT", self.url + f'/{id}', json=payload, headers=self.headers)


