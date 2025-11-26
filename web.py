import streamlit as st
import functions
from pathlib import Path

todo_file = Path("todo.txt")
if not todo_file.exists():
    with open("todo.txt", "w") as file:
        pass

todo_list = functions.get_todo()
def add_todo():
    new_task = st.session_state["new_task"]
    if new_task:
        functions.add_todo(new_task)
        st.session_state["new_task"] = ""
st.title("My Todo App") 
st.subheader("This is my todo app.")
for index, item in enumerate(todo_list):
    check = st.checkbox(item, key=f"{item}{index}")
    if check:
        todo_list.pop(index)
        with open('Todo.txt','w') as f:
            f.writelines(todo_list)
        del st.session_state[f"{item}{index}"]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", key="new_task",on_change=add_todo)