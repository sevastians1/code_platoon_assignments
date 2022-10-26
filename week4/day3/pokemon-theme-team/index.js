let pokemonChosen = 0



const getRandomPokemon = async () => {
    // let randNum = Math.floor(Math.random() * length())
    // console.log('yes!')
    let pokemonData = await axios.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
        .then((res) => {
            
            let response = res.data.results

            let randNum = Math.floor(Math.random() * response.length)
            
            let randPokemon = response[randNum]

            // pokemonChosen = randPokemon.name
            // console.log(pokemonChosen)

            // console.log(randPokemon)
            return randPokemon

        }).catch((error) => {
            console.log('No good: ', error)
        })

    let randomPokemonType = await axios.get(`${pokemonData.url}`)
        .then((res) => {
            let response = res.data.types[0].type
            // this.pokemonTypeURL = pokemonType.url
            // console.log(response)
            return response
        }).catch((error) => {
            console.log('No good: ', error)
        })
    
    // console.log(pokemonData.name)
    // console.log(randomPokemonType.name)

    document.getElementById('rand-pokemon-name').innerHTML = `Name: ${pokemonData.name}`
    document.getElementById('rand-pokemon-type').innerHTML = `Type: ${randomPokemonType.name}`

    // console.log(pokemonData.name, randomPokemonType.name)

    return randomPokemonType

}


const getSimilarPokemonType = async () => {
    
    let randPokemonType = await getRandomPokemon()

    console.log(randPokemonType)

    let poke_arr = []

    let similarPokemon = await axios.get(`${randPokemonType.url}`)
        .then((res) => {
            let response = res.data.pokemon
            
            for (let i = 0; i < 5; i++) {
                poke_arr.push(response[i].pokemon.name)
            }



        })
    
        console.log(poke_arr)



}