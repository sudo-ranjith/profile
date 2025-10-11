async function sendMessage() {
    const input = document.getElementById("userInput").value;
    const response = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ message: input })
    });
    const data = await response.json();
    const chatLog = document.getElementById("chatLog");
    chatLog.innerHTML += `<p><b>You:</b> ${input}</p>`;
    chatLog.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;
}

async function downloadResume() {
    const res = await fetch("/resume/download");
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "Ranjith_Resume.pdf";
    a.click();
    document.getElementById("status").innerText = "✅ Resume downloaded!";
}
