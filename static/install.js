// install.js

(function() {
  let deferredPrompt;

  console.log("Install script running");

  window.addEventListener('load', initialize);

  function initialize() {
    window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    const installButton = document.getElementById('installButton');
    installButton.style.display = 'none';
    installButton.addEventListener('click', showPrompt);
  }

  function handleBeforeInstallPrompt(event) {
    event.preventDefault();
    deferredPrompt = event;
    const installButton = document.getElementById('installButton');
    installButton.style.display = 'block';
  }

  function showPrompt() {
    if (deferredPrompt) {
      deferredPrompt.prompt();
    }
  }
})();
