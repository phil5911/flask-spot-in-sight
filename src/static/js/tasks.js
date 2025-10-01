// Création d'un élément dans le python => création d'une task

document.getElementById('add-task-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const id:number = 1;

    fetch("http://127.0.0.1:5000/api/task", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        title: title,
        description: description,
        id: id
    })
})
.then(res => {
    console.log("Status:", res.status);   // <== voir le code HTTP
    return res.text();                    // lire la réponse brute
})
.then(text => {
    console.log("Réponse brute:", text);  // voir si c’est bien du JSON
    try {
        const data = JSON.parse(text);
        console.log("JSON:", data);
    } catch (e) {
        console.error("⚠️ Pas du JSON valide:", e);
    }
})
.catch(err => console.error("Erreur Fetch:", err));
