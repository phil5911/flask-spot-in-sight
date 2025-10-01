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
            id: id
        })
    })
            .then(() => {
            document.getElementById('title').value = '';
            document.getElementById('description').value = '';
        })
})