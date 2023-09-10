
window.addEventListener('beforeinstallprompt',function(e) {
    console.log("Install Prompt Done.")
    downloadNav = document.getElementById('download')
    downloadNav.style.display = 'block'
})

console.log("Install Prompt Done.")