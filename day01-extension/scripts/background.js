chrome.runtime.onInstalled.addListener(() => {
  console.log("Extension installed");
  // Initialize click count to 0 if it doesn't exist
  chrome.storage.local.get(["clickCount"], function (result) {
    if (typeof result.clickCount === "undefined") {
      chrome.storage.local.set({ clickCount: 0 });
    }
  });
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.message === "button_clicked") {
    console.log("Button clicked received:", request.button);

    // Get the current click count
    chrome.storage.local.get(["clickCount"], function (result) {
      let count = result.clickCount || 0;
      count++;

      // Update the click count
      chrome.storage.local.set({ clickCount: count }, function () {
        console.log("Total button clicks:", count);
      });
    });
    // Return true to indicate you will respond asynchronously
    return true;
  } else if (request.message === "rickrolled") {
    console.log("Rickroll'd");
    chrome.storage.local.set({ clickCount: 0 });
  }
});
