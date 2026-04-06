// Extracts visible page text (no HTML, no cookies, no DOM references sent).
// Sends to BiasLens API and posts result back to popup via chrome.runtime.

function extractText() {
  return document.body.innerText.trim();
}

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message.type === "GET_TEXT") {
    sendResponse({ text: extractText() });
  }
});
