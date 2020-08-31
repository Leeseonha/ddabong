const mysql = require('mysql');


const db = mysql.createPool({
    host :'ddabong.ckksgmnbr3dl.us-east-2.rds.amazonaws.com',
    port: '3306',
    user:'jesh',
    password:'jesh2728',
    database:'ddabong'
});

module.exports = db;