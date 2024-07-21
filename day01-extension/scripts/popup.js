document.addEventListener('DOMContentLoaded', function() {
    // Get the current click count from chrome.storage
    chrome.storage.local.get(['clickCount'], function(result) {
      let count = result.clickCount || 0;
      document.getElementById('count').textContent = count;
    });
  });
  