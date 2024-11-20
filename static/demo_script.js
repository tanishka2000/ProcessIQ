const chatBox = document.getElementById('chat-box');
const questionInput = document.getElementById('question');
const submitButton = document.getElementById('submit');

// Method to display the image and its caption
function displayImage(imageUrl) {
    // Determine if p_id_data exists, if yes display the generated image, else default image
    const caption = imageUrl
        ? 'Here is the AI-generated P&Id'
        : 'This is a default P&Id. Error: No elements found in the prompt';

    const img = document.createElement('img');
    img.src = imageUrl || 'static/default-image.jpg';  // Default image if no URL is provided
    img.style.maxWidth = '50%';  // Ensure the image is responsive
    img.style.display = 'block';  // Ensure the image is displayed properly
    img.style.margin = '0% 5%';

    const captionDiv = document.createElement('div');
    captionDiv.classList.add('message', 'bot');
    captionDiv.style.textAlign = 'center';
    captionDiv.innerHTML = caption;

    // Return the image and caption div as a tuple
    return { img, captionDiv };
}

// Method to add a message to the chat box
function addMessage(role, text, imageUrl) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', role);

    // Add text message
    if (role === 'user') {
        messageDiv.innerHTML = `<span class="userinput">${text}</span>`;
    } else if (role === 'bot') {
        messageDiv.style.display = 'block';
        const { img, captionDiv } = displayImage(imageUrl);

        // Append the image and caption to the messageDiv
        messageDiv.innerHTML = `<img src="static/chatbot-icon.png" alt="Chatbot Icon" class="bot-icon" /><span>${text}</span>`;
        messageDiv.appendChild(captionDiv);
        messageDiv.appendChild(img);
    }

    // Call displayImage to get the image and caption div
    if (role === 'bot') {

    }

    // Append the messageDiv to the chatBox and scroll to the latest message
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll to the latest message
}

// Handle submit button click
submitButton.addEventListener('click', () => {
    const question = questionInput.value.trim();
    if (!question) return;

    // Display user message
    addMessage('user', question);
    questionInput.value = '';  // Clear the input field

    // Fetch the bot's response
    fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question })
    })
    .then(response => response.json())
    .then(data => {
        if (data.genai_response) {
            // Display the bot's response
            addMessage('bot', data.genai_response, data.p_id_data);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        addMessage('bot', 'Error connecting to the server.');
    });
});
