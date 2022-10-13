
console.log("Script attached successfully")
const URL = "https://pokeapi.co/api/v2/pokemon/"

function getPoke(event) {
    event.preventDefault()
    console.log("Submitted")
    const pokeResultDiv = document.querySelector("#pokeResult")
    pokeResultDiv.innerHTML = "Loading......"
    const pokeName = document.querySelector("#pokeName").value
    console.log(pokeName)
    fetch(URL + pokeName)
        .then(response => response.json())
        .then(pokeData => {
            console.log(pokeData)
            pokeResultDiv.innerHTML = `
            <h3> Number ${pokeData.id} ${pokeData.name} </h3>
            <img src="${pokeData.sprites.front_default}">
            <h2>Type(s):</h2>
            `
            for (type of pokeData.types) {
                console.log(type.type.name)
                pokeResultDiv.innerHTML += `<p>${type.type.name}</p>`
            }
        })
        .catch(err => console.log(err))
}

async function randPoke(event) {
    console.log("connectd function")
    const pokeResultDiv = document.querySelector("#pokeResult")
    pokeResultDiv.innerHTML = "Loading......"
    let rand = Math.floor(Math.random() * 900)
    let response = await fetch(URL + rand)
    let pokeData = await response.json()
    console.log(pokeData)
    pokeResultDiv.innerHTML = `
            <h3> Number ${pokeData.id} ${pokeData.name} </h3>
            <img src="${pokeData.sprites.front_default}">
            <h2>Type(s):</h2>
            `
    for (type of pokeData.types) {
        console.log(type.type.name)
        pokeResultDiv.innerHTML += `<p>${type.type.name}</p>`
    }

}