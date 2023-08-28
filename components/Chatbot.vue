<template>
  <div ref="draggable" class="draggable-box">
    <div class="bg-white rounded-lg shadow-lg p-4 max-w-sm h-full flex flex-col">
      <div class="overflow-y-auto flex-grow p-2 custom-scrollbar">
        <div v-for="message in messages" :class="messageClass(message.sender)" v-html="message.text"></div>
      </div>
      <!-- Conditional rendering for user input -->
      <div v-if="currentOptions.length > 0">
        <button v-for="option in currentOptions" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="selectOption(option)">
          {{ option }}
        </button>
      </div>
      <div v-else-if="isNumberInput">
        <select v-model="selectedCountryCode">
          <option v-for="code in currentOptions" :value="code">
            {{ code }}
          </option>
        </select>
        <input type="number" v-model="userContactNumber" />
        <button @click="collectNumber">Submit</button>
      </div>
      <div v-else>
        <textarea
          v-model="userInput"
          class="w-full p-2 border rounded"
          placeholder="Type your message..."
          rows="2"
          ></textarea>
        <button class="bg-blue-500 hover:bg-blue-600 text-white p-2 mt-2 rounded" @click="sendMessage('user', userInput)">Send</button>
      </div>
    </div>
  </div>
</template>
<script>
import countryCodes from '@/data/countrycode.json';
import axios from 'axios';
export default {
  data() {
    return {
      showChat: true,  // Chat is initially visible
      dragging: false,
      pos: { x: 0, y: 0 },
      userInput: '',
      messages: [],
      currentOptions: [],
      personalInfo: {
        name: '',
        contact: '',
        query: ''
      },      
      state: 'initial',
      countryCodes: countryCodes,
    selectedCountryCode: '+1',
    };
  },
  mounted() {
    // Set showChat to true when the component is mounted
    this.startConversation();
    
    let chatWindow = this.$refs.draggable;
    let offsetX, offsetY, dragged = false;

    chatWindow.addEventListener("mousedown", (e) => {
      dragged = true;
      offsetX = e.clientX - chatWindow.getBoundingClientRect().left;
      offsetY = e.clientY - chatWindow.getBoundingClientRect().top;

      const onMouseMove = (e) => {
        if (dragged) {
          chatWindow.style.position = "fixed";
          chatWindow.style.left = `${e.clientX - offsetX}px`;
          chatWindow.style.top = `${e.clientY - offsetY}px`;
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
    startConversation() {
      this.state = 'initial';
      this.sendMessage('bot', 'Hey there! Would you like to schedule an appointment?');
      this.currentOptions = ['Yes', 'No']; // Enable buttons for the initial state
    },
    sendMessage(sender, message) {
    this.messages.push({ sender: sender, text: message });
  },


    selectOption(option) {
      this.sendMessage('user', option);  // Reflect the button text as a user message

      switch (this.state) {
        case 'initial':
          this.personalInfo.name = option;
          this.sendMessage('bot', `Nice to meet you, ${this.personalInfo.name}. Can you please provide your contact number?`);
          this.state = 'collectContact';
          this.currentOptions = [];  // Switch to text input
          break;

        case 'collectContact':
          this.personalInfo.contact = option;
          this.sendMessage('bot', `Great, got it. Do you have a specific query or issue you'd like to discuss?`);
          this.state = 'collectQuery';
          this.currentOptions = [];  // Switch to text input
          break;

        case 'collectQuery':
          this.personalInfo.query = option;
          this.sendMessage('bot', `Would you like to schedule a call now or would you prefer a callback?`);
          this.state = 'scheduleOrCallback';
          this.currentOptions = ['Schedule Now', 'Callback Later'];  // Switch to buttons
          break;

        case 'scheduleOrCallback':
          if (option === 'Schedule Now') {
            this.fetchTimeSlots();
          } else {
            this.sendMessage('bot', `Great, we'll call you back. Thanks!`);
            // Here, you can create a callback query on the backend
          }
          break;

        // Add more states if needed

        default:
          this.sendMessage('bot', `I'm sorry, I didn't understand that.`);
          break;
      }
    },

    fetchTimeSlots() {
      axios.get('http://localhost:5000/api/timeslots')
        .then(response => {
          this.currentOptions = response.data;
          this.state = 'showTimeSlots';
          this.sendMessage('bot', 'Here are the available time slots.');
        })
        .catch(error => {
          console.error("An error occurred while fetching data: ", error);
        });
    },
    toggleChat() {
      this.showChat = !this.showChat;
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
  width: 0;
  /* Remove scrollbar */
}

.overflow-hidden-scrollbar::-webkit-scrollbar {
  display: none;
}

.overflow-hidden-scrollbar {
  scrollbar-width: none;
  /* For Firefox */
}
.draggable-box {
  position: fixed;}
/* Modify the bubble style as needed */</style>
  