async function submitQuery() {
    const query = document.getElementById('query').value;
    const responseDiv = document.getElementById('response');

    const res = await fetch('http://localhost:5000/api/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query })
    });

    const data = await res.json();
    responseDiv.innerText = data.response;
}