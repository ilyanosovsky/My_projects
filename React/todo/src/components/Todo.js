import {useState} from 'react';

const Todo = () => {

    const [todo, setTodo] = useState('');
    const [todos, setTodos] = useState([]);
  
    const handleSubmit = (e) => {
      e.preventDefault();
      if (todo.trim() !== '') {
        setTodos([...todos, { id: Date.now(), text: todo }]);
        setTodo('');
      }
    };

    const handleDelete = (id) => {
        setTodos(todos.filter((todo) => todo.id !== id));
    };

    return(
        <>
        <h1>Todo's</h1>
        <div id="todolist">
            {todos.map((item, index) => (<div className='todo-item' key={index} onClick={() => handleDelete(item.id)}>{item.text}</div>))}
        </div>
        <form onSubmit={handleSubmit}>
            <label>Add todo:</label>
            <input name='todo' value={todo} onChange={(e)=>setTodo(e.target.value)}/>
        </form>
        </>
    )
}

export default Todo;