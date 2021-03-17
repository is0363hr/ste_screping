const express = require('express')
const app = express()
const router = express.Router()
const bodyParser = require('body-parser')

// まずはルーティングのみ追加
router.post(
  '/webhook',
  // 署名検証のためテキストでパース
  bodyParser.text({ type: 'application/json' }),
  require('./routes/webhook')
)

// database接続
router.get('/meteorologic', (req, res, next) => {
  const mysql = require('mysql');
  const connection = mysql.createConnection({
    host : 'localhost',
    user : 'testuser',
    database: 'testdb',
    password: 'testuser'
  });
  var ret=[];
  connection.connect();
  connection.query('SELECT * from prefectures;', function(error, row, fields){
    if (error) {
      console.log(error);
    }
    var dat = [];
    for (var i = 0;i < row.length; i++) {
      dat.push({id: row[i].id, name: row[i].name});
    }
    ret = JSON.stringify(dat);
    res.header('Content-Type', 'application/json; charset=utf-8')
    res.send(ret)
  });
  connection.end();
})

module.exports = router