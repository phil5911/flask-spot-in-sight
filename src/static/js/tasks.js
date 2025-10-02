// Création d'un élément dans le python => création d'une task

document.getElementById('add-task-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const id = 1;
    fetch('http://127.0.0.1:5000/api/task',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            title: title,
            description: description,
        })
    })
            .then(() => {
            document.getElementById('title').value = '';
            document.getElementById('description').value = '';
            refresh();
        })
})


function refresh(){
    fetch('/api/task')
        .then(response => response.json())
            // Récupération de la table HTML
        .then(data => {
            const taskTable = document.getElementById('task-table').getElementsByTagName('tbody')[0];
            taskTable.innerHTML = '';
            data.forEach((task) => {
                const row = taskTable.insertRow();

                const titleCell = row.insertCell(0);
                titleCell.textContent = task.title;

                const descriptionCell = row.insertCell(1);
                descriptionCell.textContent = task.description;

                const statusCell = row.insertCell(2);
                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.checked = task.completed;
                checkbox.onclick = () => toggleTask(task.id,task.title,task.description,checkbox.checked);
                statusCell.appendChild(checkbox);

                const actionsCell = row.insertCell(3);
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Supprimer';
                deleteButton.onclick = () => deleteTask(task.id);
                actionsCell.appendChild(deleteButton);
            })
        })
}

function deleteTask(taskId) {
    fetch(`/api/task/${taskId}`, {
        method: 'DELETE'
    }).then(() => refresh());
}

function toggleTask(taskId, title, description, isChecked) {
    fetch(`/api/task/${taskId}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify( {
            title: title,
            description: description,
            completed: isChecked
        })
    }).then(() => refresh());
}

// chargement initial des tâches
refresh();






