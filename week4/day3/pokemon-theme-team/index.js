
const getRandomPokemon = async () => {
    // let randNum = Math.floor(Math.random() * length())
    // console.log('yes!')
    let response = await axios.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
       
    let pokemonData = response.data.results

    let randNum = Math.floor(Math.random() * pokemonData.length)
        
    let randPokemon = pokemonData[randNum]

    let randPokemonURL = randPokemon.url

    let randPokemonType = await getRandomPokemonType(randPokemonURL)
    // console.log(randPokemonType)

    let randPokemonSprite = await getRandomPokemonSprite(randPokemon.url)
    // console.log(randPokemonImage)

    document.getElementById('rand-pokemon-name').innerHTML = `Name: ${randPokemon.name}`
    document.getElementById('rand-pokemon-type').innerHTML = `Type: ${randPokemonType.name}`
    
    let docPokemonImage = document.getElementById('rand-pokemon-image')
    docPokemonImage.src = randPokemonSprite

}

const getRandomPokemonType = async (randPokemonURL) => {

    let response = await axios.get(randPokemonURL)

    let randPokemonType = response.data.types[0].type

    localStorage.setItem('pokemonType', randPokemonType.url)

    return randPokemonType
}

const getRandomPokemonSprite = async (randPokemonSprite) => {

    let response = await axios.get(randPokemonSprite)

    randPokemonImage = response.data.sprites.other['official-artwork'].front_default


    // console.log(randPokemonImage)
    return randPokemonImage

}


const getSimilarPokemonType = async () => {
    
    let randPokemonTypeURL = localStorage.getItem('pokemonType')

    // console.log(randPokemonTypeURL)

    let response = await axios.get(randPokemonTypeURL)

    let similarPokemon = response.data.pokemon

    // console.log(similarPokemon)

    let poke_arr = []

    for (let i = 0; i < 5; i++) {
        // console.log(similarPokemon[i].url)
        poke_arr.push(similarPokemon[i].pokemon)
    }
    console.log(poke_arr)

    similarPokeImage = document.getElementById('similar-poke-image')

    for (let i = 0; i < poke_arr.length; i++) {
        let pokeImage = await getRandomPokemonSprite(poke_arr[i].url)
        console.log(pokeImage)
        similarPokeImage.innerHTML += `<img src=${pokeImage} alt="poke-image"/>`
    }
    




}