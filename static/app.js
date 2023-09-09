if (navigator.serviceWorker) {

    navigator.serviceWorker.register('static/service-worker.js')
}

window.addEventListener('beforeinstallprompt',function(e) {
    downloadNav = document.getElementById('download')
    downloadNav.style.display = 'block'
})

