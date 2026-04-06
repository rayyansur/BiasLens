// Compiled to popup.js by build step.

document.getElementById("analyze-btn")!.addEventListener("click", async () => {
  const resultEl = document.getElementById("result")!;
  resultEl.textContent = "Analyzing…";

  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab.id) {
    resultEl.innerHTML = '<span class="error">No active tab.</span>';
    return;
  }

  chrome.runtime.sendMessage({ type: "ANALYZE", tabId: tab.id }, (response) => {
    if (!response.ok) {
      resultEl.innerHTML = `<span class="error">Error: ${response.error}</span>`;
      return;
    }
    const { bias, bias_score, sentiment } = response.data;
    resultEl.innerHTML = `
      <p><strong>Bias:</strong> ${bias} (${(bias_score * 100).toFixed(0)}%)</p>
      <p><strong>Sentiment:</strong> ${sentiment}</p>
    `;
  });
});
