if (navigator.serviceWorker) {

    navigator.serviceWorker.register('static/service-worker.js')
}

let deferredPrompt
window.onload = Logic
function showPrompt() {
    deferredPrompt.prompt(); 
}

// Download Button
function Logic() {

window.addEventListener('beforeinstallprompt', function(e) {
e.preventDefault();
    deferredPrompt = e

}
)
const install = document.getElementById('installButton');
install.onclick = showPrompt;


}

