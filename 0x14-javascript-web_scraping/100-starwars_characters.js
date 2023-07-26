#!/usr/bin/node

const request = require('request')
try {
    const url = `https://swapi-api.alx-tools.com/api/films/${Number(process.argv[2])}/`
request(url, (err, res, body) => {
    if (err) throw err

    const filmData = JSON.parse(body)
    const character_urls = filmData.characters
    for (const url of character_urls) {
        request(url, (err, res, body) => {
            if (err) throw err

            data = JSON.parse(body)
            console.log(data.name)
        })
    }
})
}
catch (e) {
    print(e)
}
