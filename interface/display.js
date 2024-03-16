// Открывает главное окно после регистрации или входа
eel.expose(switchToChat)
function switchToChat() {
    var signUpWindow = document.querySelector('.sign-up-window');
    var logInWindow = document.querySelector('.log-in-window');
    var chatWindow = document.querySelector('.chat-window');

    signUpWindow.style.display = 'none'; 
    logInWindow.style.display = 'none'; 
    chatWindow.style.display = 'block';
}

// Принимает данные переписок и загружает их на страницу
eel.expose(loadChatHistory)
function loadChatHistory(data) {
    setChatsData(data); 
    console.log(chatsData)
    showChats();
}

// Загружает данные переписок в словарь
function setChatsData(data) {
    chatsData = data;
}

// Функция для отображения списка чатов
function showChats() {
    var chatList = document.getElementById("chatList");
    chatList.innerHTML = "";

    chatsData.forEach(chat => {
        var chatItem = document.createElement("li");
        chatItem.classList.add("chat-item");
        chatItem.textContent = chat.name;
        chatItem.onclick = function() {
            handleChatClick(chat.id);
        };
        chatList.appendChild(chatItem);
    });
}

// Открывает окно регистрации
function switchToSignUpWindow() {
    var signUpWindow = document.querySelector('.sign-up-window');
    var logInWindow = document.querySelector('.log-in-window');
    var chatWindow = document.querySelector('.chat-window');

    signUpWindow.style.display = 'block'; 
    logInWindow.style.display = 'none'; 
    chatWindow.style.display = 'none';
}

// Открывает окно входа
function switchToLogInWindow() {
    var signUpWindow = document.querySelector('.sign-up-window');
    var logInWindow = document.querySelector('.log-in-window');
    var chatWindow = document.querySelector('.chat-window');

    signUpWindow.style.display = 'none'; 
    logInWindow.style.display = 'block'; 
    chatWindow.style.display = 'none';
}

