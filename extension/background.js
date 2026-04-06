// Service worker — coordinates between content script and popup.

const TIMEOUT_MS = 30_000;

async function analyzeTab(tabId, apiUrl, apiKey) {
  const [{ result }] = await chrome.scripting.executeScript({
    target: { tabId },
    func: () => document.body.innerText.trim(),
  });

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);

  try {
    const response = await fetch(`${apiUrl}/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({ text: result }),
      signal: controller.signal,
    });

    if (!response.ok) throw new Error(`API error ${response.status}`);
    return await response.json();
  } finally {
    clearTimeout(timer);
  }
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "ANALYZE") {
    chrome.storage.local.get(["apiUrl", "apiKey"], ({ apiUrl, apiKey }) => {
      analyzeTab(message.tabId, apiUrl, apiKey)
        .then((data) => sendResponse({ ok: true, data }))
        .catch((err) => sendResponse({ ok: false, error: err.message }));
    });
    return true; // keep message channel open for async response
  }
});
