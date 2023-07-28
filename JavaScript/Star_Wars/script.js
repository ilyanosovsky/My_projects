const randBtn = document.getElementById('randomBtn');
const divElem = document.getElementById('info');


function showLoading() {
    const div = document.createElement("div");
    div.className = "fa-3x";

    const i = document.createElement("i");
    i.className = "fa-solid fa-spinner fa-spin-pulse";

    const p = document.createElement("p");
    p.textContent = "Loading...";

    div.appendChild(i);

    divElem.appendChild(div);
    divElem.appendChild(p);

}


const getPerson = async () => {
    try {
        let endpoint = "https://www.swapi.tech/api/people/" + getNum(); //+ getRandomInt(1, 84)
        const response = await fetch(endpoint);
        if (response.ok){
            data = await response.json();
        } else {
            throw new Error("Oh No! That person isn't available.")
        }
        return data.result;
    } catch (err) {
        return err;
    }
}


const getPlanet = async (id) => {
    try {
        let endpoint = "https://www.swapi.tech/api/planets/" + id;
        const response = await fetch(endpoint);
        
        if (response.ok){
            data = await response.json();
        } else {
            throw new Error("Something went wrong...")
        }
        console.log(data.result.properties.name);
        return data.result.properties.name;
    } catch (err) {
        return err;
    }
}

function getNum () {
    let num = Math.floor(Math.random() * 83) + 1;
    return num
}

randBtn.addEventListener("click", function (event) {
    divElem.textContent = "";

    ( async () => {
        showLoading();
        // await showLoading();
        let character = await getPerson();

        if (character instanceof Error) {
            const error = document.createElement("h1");
            error.textContent = character.message;
            divElem.textContent = "";
            divElem.appendChild(error);
        } else {
            character = character.properties;

            const planetId = /[^/]*$/.exec(character.homeworld)[0];

            let planet = await getPlanet(planetId);

            console.log(planet);

            const name = document.createElement("h1");
            name.textContent = character.name;

            const height = document.createElement("p");
            height.textContent = `Height: ${character.height}`;

            const gender = document.createElement("p");
            gender.textContent = `Gender: ${character.gender}`;

            const birthYear = document.createElement("p");
            birthYear.textContent = `Birth Year: ${character.birth_year}`;

            const homeWorld = document.createElement("p");
            homeWorld.textContent = `Home World: ${planet}`;

            divElem.textContent = "";
            divElem.appendChild(name);
            divElem.appendChild(height);
            divElem.appendChild(gender);
            divElem.appendChild(birthYear);
            divElem.appendChild(homeWorld);
        }
    } )();
 });