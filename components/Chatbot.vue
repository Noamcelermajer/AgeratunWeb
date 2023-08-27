<template>
  <div ref="draggable" class="draggable-box">
    <div class="bg-white rounded-lg shadow-lg p-4 max-w-sm h-full flex flex-col" v-if="showChat">
      <div class="flex justify-between items-center border-b pb-2">
        <h2 class="text-lg font-bold">Virtual Assistant</h2>
        <button class="text-gray-500 hover:text-gray-700" @click="toggleChat">&times;</button>
      </div>
      <div class="overflow-y-auto flex-grow p-2 custom-scrollbar">
        <div v-for="message in messages" :class="messageClass(message.sender)" v-html="message.text"></div>
      </div>
      <div v-if="currentOptions.length > 0">
        <button v-for="option in currentOptions" @click="selectOption(option)">
          {{ option }}
        </button>
      </div>
      <div class="pt-2 flex-none">
        <textarea
          v-model="userInput"
          @keydown.enter.prevent="addNewLine"
          class="w-full p-2 border rounded"
          placeholder="Type your message..."
          rows="2"
          ></textarea>
        <button class="bg-blue-500 text-white p-2 mt-2 rounded hover:bg-blue-600" @click="sendMessage">Send</button>
      </div>
    </div>
  </div>
</template>
  <script>
  export default {
    data() {
      return {
            // Other data properties
            showChat: false, 
    dragging: false,
    pos: { x: 0, y: 0 },
        showChat: false,
        userInput: '',
        messages: [
          { sender: 'bot', text: 'Hey there! How are you doing today? 😊' },
        ],
      };
    },
    mounted() {
    // Set showChat to true when the component is mounted
    this.showChat = true;
    const chatWindow = this.$refs.draggable;
    
    // Set the initial position
    chatWindow.style.left = "auto";
    chatWindow.style.right = "20px";
    chatWindow.style.bottom = "20px";
    chatWindow.style.top = "auto";

    let dragged = false;

    chatWindow.addEventListener("mousedown", (e) => {
      dragged = true;

      let offsetX = e.clientX - chatWindow.getBoundingClientRect().left;
      let offsetY = e.clientY - chatWindow.getBoundingClientRect().top;

      const onMouseMove = (e) => {
        if (dragged) {
          chatWindow.style.right = "auto";  // Reset these so they don't interfere
          chatWindow.style.bottom = "auto"; // Reset these so they don't interfere
          chatWindow.style.left = e.clientX - offsetX + "px";
          chatWindow.style.top = e.clientY - offsetY + "px";
        }
      };

      document.addEventListener("mousemove", onMouseMove);

      chatWindow.addEventListener("mouseup", () => {
        dragged = false;
        document.removeEventListener("mousemove", onMouseMove);
      });
    });
    },
    methods: {
      toggleChat() {
        this.showChat = !this.showChat;
      },
      sendMessage() {
        const formattedMessage = this.userInput.replace(/\n/g, '<br>');
        this.messages.push({ sender: 'user', text: formattedMessage });
        this.userInput = '';
        this.messages.push({ sender: 'bot', text: 'Thank you for your response!' });
      },
      addNewLine() {
        this.userInput += '\n';
    },
      messageClass(sender) {
        return sender === 'bot'
          ? 'text-gray-800 my-2 w-full max-w-[40%] bg-gray-200 rounded-lg ml-2 px-3 py-2'
          : 'text-white my-2 w-full max-w-[40%] bg-blue-600 ml-auto rounded-lg mr-2 px-3 py-2';
      },
      startDrag(event) {
    this.dragging = true;
    this.pos = {
      x: event.clientX - this.$refs.draggable.offsetLeft,
      y: event.clientY - this.$refs.draggable.offsetTop
    };
  },
  doDrag(event) {
    if (this.dragging) {
      this.$refs.draggable.style.left = event.clientX - this.pos.x + 'px';
      this.$refs.draggable.style.top = event.clientY - this.pos.y + 'px';
    }
  },
  stopDrag() {
    this.dragging = false;
  }
    },
  };
  </script>
  <style scoped>
  .custom-scrollbar::-webkit-scrollbar {
    width: 0; /* Remove scrollbar */
  }
  .overflow-hidden-scrollbar::-webkit-scrollbar {
    display: none;
  }
  .overflow-hidden-scrollbar {
    scrollbar-width: none; /* For Firefox */
  }
  /* Modify the bubble style as needed */
  </style>
  