 const boldBtn = document.querySelector("#bold-btn")
const underlineBtn = document.querySelector("#underline-btn")
const italicBtn = document.querySelector("#italic-btn")
const colorBtn = document.querySelector("#color-btn")

const copyBtn=document.querySelector("#copy-btn")
const cutBtn=document.querySelector("#cut-btn")
const pasteBtn=document.querySelector("#paste-btn")

const newBtn = document.querySelector("#new-btn")
const txtBtn = document.querySelector("#txt-btn")
const pdfBtn = document.querySelector("#pdf-btn")

const content = document.querySelector("#content")
const filename = document.querySelector("#filename-input")

const spellBtn=document.querySelector("spell-btn")

// spellBtn.addEventListener("click",() => {
//     document.getElementById("content").innerHTML="Hello";
// })  
copyBtn.addEventListener("click",() => {
    document.execCommand("copy")
})
cutBtn.addEventListener("click",() => {
    document.execCommand("cut")
})
// pasteBtn.addEventListener("paste", function(e) {
//     // cancel paste
//     e.preventDefault();

//     // get text representation of clipboard
//     var text = (e.originalEvent || e).clipboardData.getData('text/plain');

//     // insert text manually
//     document.execCommand("paste", false, text);
// });

boldBtn.addEventListener("click", () => {
    document.execCommand("bold")
})

underlineBtn.addEventListener("click", () => {
    document.execCommand("underline")
})

italicBtn.addEventListener("click", () => {
    document.execCommand("italic")
})

colorBtn.addEventListener("input", () => {
    document.execCommand("forecolor", false, colorBtn.value)
})

newBtn.addEventListener("click", () => {
    content.innerHTML = ""
})

txtBtn.addEventListener("click", () => {
    const a = document.createElement("a")
    const blob = new Blob([content.innerText])
    const dataUrl = URL.createObjectURL(blob)
    a.href = dataUrl
    a.download = filename.value + ".txt"
    a.click()
})


