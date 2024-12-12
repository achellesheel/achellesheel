async function askBot() {
    const query = document.getElementById('user-query').value;
    const responseDiv = document.getElementById('bot-response');
    
    if (!query) {
        responseDiv.innerHTML = '<span style="color: red;">Please enter a question.</span>';
        return;
    }

    responseDiv.innerHTML = '<em>Loading...</em>';
    try {
        const response = await fetch('http://127.0.0.1:5000/faq', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        responseDiv.innerHTML = `
            <strong>Answer:</strong> ${data.answer}<br>
            <strong>Confidence:</strong> ${data.confidence.toFixed(2)}
        `;
    } catch (error) {
        responseDiv.innerHTML = `<span style="color: red;">Error: ${error.message}</span>`;
    }

}
