// Загрузка чатов при загрузке страницы
window.onload = function() {
    showChats();
};

var openedChatID = -1

// Пример данных чатов (замените на реальные данные)
var chatsData = [
    { id: 34, name: "Чат 1", messages: [
        {
            time: "12:20",
            content: "Hello World!",
            sender_name: "Sergey"
        }, 
        {
            time: "12:23",
            content: "Hi there!",
            sender_name: "Alex"
        }] 
    },
    { id: 53, name: "Чат 2", messages: [] },
    { id: 12, name: "Чат 3", messages: [] }
];


// Добавляет в список новое сообщение
eel.expose(addNewMessage)
function addNewMessage(chatId, time, content, sender_name) {
    console.log(chatId)
    console.log(time)
    console.log(content)
    console.log(sender_name)

    var activeChat = chatsData.find(chat => chat.id === chatId);

    if (activeChat) {
        activeChat.messages.push(
            {time: time,
            content: content,
            sender_name: sender_name}
        );

        if (openedChatID == activeChat.id) {
            displayChat(openedChatID);
        }
    }
    else {
        console.log("Chat not found");
    }
}


eel.expose(addNewChat) 
function addNewChat(chat_id, chat_name) {
    // Проверяем, есть ли уже чат с таким ID
    var existingChat = chatsData.find(chat => chat.id === chat_id);

    if (existingChat) {
        console.log("Chat with ID " + chat_id + " already exists.");
    } else {
        // Создаем новый чат
        var newChat = {
            id: chat_id,
            name: chat_name,
            messages: []
        };

        // Добавляем новый чат в массив chatsData
        chatsData.push(newChat);
        console.log("New chat added: ", newChat);

        console.log(chatsData);
        showChats();

        displayChat(chat_id);
    }
}


// Функция для открытия чата
function displayChat(chatId) {
    var chatContent = document.getElementById("chatContent");
    var activeChat = chatsData.find(chat => chat.id === chatId);
    chatContent.innerHTML = "<h2>" + activeChat.name + "</h2>";

    activeChat.messages.forEach(message => {
        chatContent.innerHTML += "<div class='message'>" + "[" + message.sender_name + "] " + message.content + " " + message.time + "</div>";
    });

    var userID = parseInt(document.getElementById('userID').innerText);
    console.log(userID);
    
    var messageInput = document.getElementById('chatID');
    messageInput.innerText = activeChat.id;

    openedChatID = activeChat.id;
}

// Функция для обработки клика на чат
function handleChatClick(chatId) {
    displayChat(chatId);

    document.getElementById("message-input-div").style = "display: block"; 
    document.getElementById("add-member-div").style = "display: block";
}

// Нажатие кнопки "Зарегистрироваться"
function signUp() {
    var name = document.getElementById('sign-up-name').value;
    var password = document.getElementById('sign-up-password').value;

    eel.sign_up(name, password);

    document.getElementById('sign-up-name').value = '';
    document.getElementById('sign-up-password').value = '';
}

// Нажатие кнопки "Войти"
function logIn() {
    var name = document.getElementById('log-in-name').value;
    var password = document.getElementById('log-in-password').value;

    eel.log_in(name, password);

    document.getElementById('log-in-name').value = '';
    document.getElementById('log-in-password').value = '';
}

// Нажатие кнопки "Отправить сообщение"
function sendMessage() { // ID отправителя, ID чата, текст сообщения.
    var userID = parseInt(document.getElementById('userID').innerText);
    var chatID = parseInt(document.getElementById('chatID').innerText);
    var content = document.getElementById('messageInput').value;

    eel.send_message_to_server(content, userID, chatID);
    document.getElementById('messageInput').value = '';
}


// Сохраняет ID пользователя
eel.expose(loadUserID)
function loadUserID(user_id) {
    document.getElementById('userID').innerText = user_id
}

eel.expose(createNewChat)
function createNewChat() {
    var chatName = document.getElementById('newChatName').value; 

    eel.create_new_chat(chatName);
    var chatName = document.getElementById('newChatName').value = "";
}

eel.expose(createNewChatMember)
function createNewChatMember() {
    var newMemberID = parseInt(document.getElementById('newMemberInput').value);
    var chatID = parseInt(document.getElementById('chatID').innerText); 

    document.getElementById('newMemberInput').value = "";

    eel.create_new_chat_member(chatID, newMemberID)
}