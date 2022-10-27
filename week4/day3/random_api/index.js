

const getAPI = async () => {

    url = 'https://api.roadgoat.com/api/v2/destinations/new-york-ny-usa'

    const response = await axios.get(url, {
        auth: {
            username: '4ff3dabbbb83ee9fcda38a3da0be4b63',
            password: 'c04377692994c69c4aa68c022c514057'
        }
    })

    console.log(response.data)

}