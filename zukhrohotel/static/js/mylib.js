const loader = document.querySelector(".loader-content")

document.addEventListener("DOMContentLoaded",()=>laoder())

const COMMONDS = [73, 85, 80, 123];

// WINDOWS KEY COMMONDS
// F12 => 123(developer tools)
// Ctrl + Shift + I => 73(developer tools)
// Ctrl + U => 85(web sahifa codeni yangi oynada ko'rish)
// Ctrl + P => 80(Web sahifani chop etish)

window.addEventListener("contextmenu", (e) => e.preventDefault());
window.addEventListener("keydown", (e) => {
    if(COMMONDS.includes(e.keyCode)) {
        e.preventDefault()
    }
})


function laoder() {
    setTimeout(()=>{
        loader.classList.add("loader-time")
        setTimeout(() => {
            loader.style.display = "none"
        },2000)
    },1000)
}