const searchInput = document.getElementById('search-input');
const searchBtn = document.getElementById('search-btn');
const micBtn = document.getElementById('mic-btn');

// Check if speech recognition is supported by the browser
if ('webkitSpeechRecognition' in window) {
  const recognition = new webkitSpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.lang = 'en-US';

  micBtn.addEventListener('click', () => {
    recognition.start();
  });

  recognition.onresult = (event) => {
    const result = event.results[0][0].transcript;
    searchInput.value = result;
    searchBtn.click();
  };
}