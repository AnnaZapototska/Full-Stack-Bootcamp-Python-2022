// Recreate the todo list above:

// Create an HTML, CSS and a JS file.

// In the HTML file
// create a form with one input type="text", and a “Submit” button.
// add an empty div below the form
// <div class="listTasks"></div>

// In the js file, you must add the following functionalities:
// Create an empty array : const tasks = [];

// Create a function called addTask(). As soon as the user clicks on the button:
// check that the input is not empty,
// then add it to the array (ie. add the text of the task)
// then add it to the DOM, below the form (in the <div class="listTasks"></div>) .
// Each new task added should have (starting from left to right - check out the image at the top of the page)
// a “X” button. Use font awesome for the “X” button.
// an input type="checkbox". The label of the input is the task added by the user.
const tasks = [];
let taskInput = document.getElementById('newTask');
let addTask = document.getElementById('addTask');


function addTask(){
  if (!taskInput.value){
    return alert('Please enter the task!')
  }

}





let tasks = [];
let lastTaskID = 0;

let listTasks = document.querySelector('.listTasks');
let newTask = document.getElementById('newTask');
let addButton = document.getElementById('addButton');
let clearButton = document.getElementById('clearButton');

clearButton.addEventListener('click', (event) => {
    tasks = [];
    for (let i = listTasks.children.length - 1; i < listTasks.children.length; i--) {
        listTasks.removeChild(listTasks.children[i]);
        
    }
})

addButton.addEventListener('click', (event) => { 
    if (newTask.value == '' || newTask.value == 'NEW TASK') {
        alert('Enter name of task!');
        return;
    }   

    let taskObject = {
        task_id: 'task_' + lastTaskID,
        text: newTask.value,     
        done: false
    }
    tasks.push(taskObject);

    let div = document.createElement('div');
    let button = document.createElement('button'); 
    let checkbox = document.createElement('input');
    let label = document.createElement('label');
    button.addEventListener('click', deleteTask);
    button.innerHTML = "x";
    button.classList.add('delete-task');
    checkbox.setAttribute('type', 'checkbox');
    checkbox.classList.add('checkbox-task');
    checkbox.addEventListener('click', finishTask)
    label.innerHTML = taskObject.text;
    label.classList.add('label-task');
    div.classList.add('task');
    div.setAttribute('id', taskObject.task_id);
    div.setAttribute('data-task-id', taskObject.task_id);
    div.appendChild(button);
    div.appendChild(checkbox);
    div.appendChild(label);
    listTasks.appendChild(div);

    newTask.value = 'NEW TASK';
    lastTaskID += 1;
    event.preventDefault();
});

function deleteTask(event) {
    let div = document.getElementById(event.target.parentElement.id);
    listTasks.removeChild(div); 

    let object = tasks.find(task => task.task_id === event.target.parentElement.id);
    tasks.slice(tasks.indexOf(object), 1);
}

function finishTask(event) {
    let div = document.getElementById(event.target.parentElement.id);
    div.children[2].classList.toggle('crossed');
    let object = tasks.find(task => task.task_id === event.target.parentElement.id);
    object.done = !object.done;
}
