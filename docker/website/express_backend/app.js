const express = require('express')
const app = express()
const cors = require('cors')

const port = 3000

const cellTowersRouter = require('./routes/cellTowers')


app.use(cors())

app.use('/cellTowers', cellTowersRouter);

app.use(express.static('/express_backend/dist'));

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})