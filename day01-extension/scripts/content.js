console.log("Extension content loaded");

document.addEventListener("click", function (event) {
  if (event.target.tagName === "BUTTON") {
    console.log("BUTTON CLICKED:", event.target);

    // roll dice
    const roll = Math.random()
    if (roll < .02) {
      // unlucky
      chrome.runtime.sendMessage(
        { message: "rickrolled" },
        function (response) {}
      );
      window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
    } else {
      // forward button click to background worker
      chrome.runtime.sendMessage(
        { message: "button_clicked", button: event.target.innerText },
        function (response) {}
      );
    }
  }
});
