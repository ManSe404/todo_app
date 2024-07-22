import streamlit as st
import functions

TODOS = functions.open_todos("todos.txt")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    TODOS.append(todo)
    functions.write_todos(TODOS)


st.title("ToDo App")
st.subheader("Improving daily organization")
st.write("Write, update and complete todos to improve productivity")

for index, todo in enumerate(TODOS):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        TODOS.pop(index)
        functions.write_todos(TODOS)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", 
              placeholder="Add new todo ...",
              on_change=add_todo, 
              key="new_todo")
