const chatContainer = document.getElementById("chat-container");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const clearBtn = document.getElementById("clear-btn");

const API_URL = "http://127.0.0.1:8000/chat";

function addMessage(text, sender) {
    const wrapper = document.createElement("div");
    wrapper.classList.add("message", sender);

    const inner = document.createElement("div");
    inner.innerText = text;

    wrapper.appendChild(inner);
    chatContainer.appendChild(wrapper);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}



function showTyping() {
    const typingDiv = document.createElement("div");
    typingDiv.classList.add("message", "bot");
    typingDiv.id = "typing";

    typingDiv.innerHTML = `
        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

    chatContainer.appendChild(typingDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function removeTyping() {
    const typingDiv = document.getElementById("typing");
    if (typingDiv) typingDiv.remove();
}

async function sendMessage() {
    const question = userInput.value.trim();
    if (!question) return;

    addMessage(question, "user");
    userInput.value = "";
    sendBtn.disabled = true;

    showTyping();

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        removeTyping();
        addMessage(data.answer || "Unexpected response.", "bot");
    } catch {
        removeTyping();
        addMessage("Connection error.", "bot");
    }

    sendBtn.disabled = false;
}

clearBtn.addEventListener("click", () => {
    chatContainer.innerHTML = `
        <div class="message bot">
            Chat cleared. Ask a new Machine Learning question.
        </div>
    `;
});

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keydown", e => {
    if (e.key === "Enter") sendMessage();
});
// Sparkle generator
const sparkleContainer = document.querySelector(".sparkle-container");

function createSparkle() {
    const sparkle = document.createElement("div");
    sparkle.classList.add("sparkle");
    sparkle.style.left = Math.random() * window.innerWidth + "px";
    sparkle.style.animationDuration = (3 + Math.random() * 3) + "s";
    sparkleContainer.appendChild(sparkle);

    setTimeout(() => sparkle.remove(), 6000);
}

setInterval(createSparkle, 400);
