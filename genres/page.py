import streamlit as st

genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comédia'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]


def show_genres():
    st.write('Lista de Gêneros')

    st.table(genres)

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso!')
