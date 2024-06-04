import requests
import streamlit as st
from login.service import logout


class GenreRepository:

    def __init__(self):
        self.__base_url = 'https://juliogazoli.pythonanywhere.com/api/v1/'
        self.__genre_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(
            self.__genre_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {
                        response.status_code}')
