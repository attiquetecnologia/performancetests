const express = require('express')
const app = express()
const port = 8000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get("/api", (req, res) =>{
    res.send([
        {'id': 1, 'name': 'Ronald'},
        {'id': 2, 'name': 'Ronald'},
        {'id': 3, 'name': 'Ronald'},
        {'id': 4, 'name': 'Ronald'},
        {'id': 5, 'name': 'Ronald'},
        {'id': 6, 'name': 'Ronald'},
        {'id': 7, 'name': 'Ronald'},
        {'id': 8, 'name': 'Ronald'},
        {'id': 9, 'name': 'Ronald'},
        {'id': 10, 'name': 'Ronald'},
    ])
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
