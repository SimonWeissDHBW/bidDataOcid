const express = require('express')
const app = express()
const cors = require('cors')
const mysql_connector = require('mysql2')

const port = 3000

const cellTowersRouter = require('./routes/cellTowers')

db = mysql_connector.createConnection({
    host : 'ocid',
    user : 'root',
    password  :'ocidBigData',
    database : 'cell_towers'
});

app.use(cors())

app.use('/cellTowers', cellTowersRouter);

app.use(express.static('/express_backend/dist'));

app.get('/', (req,res) => {
  res.sendFile('/express_backend/dist/index.html');
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})