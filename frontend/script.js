const form = document.getElementById("heroForm")

form.addEventListener("submit", async (e) => {

e.preventDefault()

document.getElementById("loading").innerHTML =
"⚡ Generating your Cloud Hero..."

const formData = new FormData(form)

const res = await fetch("/generate-avatar", {
method: "POST",
body: formData
})

const data = await res.json()

document.getElementById("loading").innerHTML = ""

document.getElementById("result").innerHTML =
`<img src="${data.image}" width="400"/>`

})