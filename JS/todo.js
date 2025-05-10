// how to make a todo app

// using javascript

const todos = [
    {
        id: 1,
        title: "Learn JavaScript",
        completed: false
    },
    {
        id: 2,
        title: "Learn React",
        completed: false
    },
    {
        id: 3,
        title: "Learn Node.js",
        completed: false
    },
    {
        id: 4,
        title: "Learn Express",
        completed: false
    },
    {
        id: 5,
        title: "Learn MongoDB",
        completed: false
    }
];
// function to add a new todo
function addTodo(title) {
    const newTodo = {
        id: todos.length + 1,
        title: title,
        completed: false
    };
    todos.push(newTodo);
}