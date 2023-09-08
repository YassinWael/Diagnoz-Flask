let deferredPrompt;

console.log("install running");

window.onload = Logic;

function showPrompt() {
  if (deferredPrompt) {
    deferredPrompt.prompt();
  }
}

// Download Button
function Logic() {
  window.addEventListener('beforeinstallprompt', function(e) {
    e.preventDefault();
    deferredPrompt = e;
    const installButton = document.getElementById('installButton');
    installButton.style.display = 'block';
  });

  const installButton = document.getElementById('installButton');
  installButton.style.display = 'none';
  installButton.onclick = showPrompt;
}
