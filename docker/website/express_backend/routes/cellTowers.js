const express = require('express'),
  router = express.Router();

// get user lists
router.get('/:radio/:lonParam/:latParam', function(req, res) {
  // console.log("Longitude: " + req.params.lonParam + "\nLatitude: " + req.params.latParam);
  // let sql = `SELECT * FROM towers WHERE radio = '${req.params.radio}' AND st_distance_Sphere(point(lon, lat), point(${req.params.lonParam}, ${req.params.latParam})) <= towers.range LIMIT 1`;
  let sql = `SELECT MIN(st_distance_Sphere(point(TowersInRange.lon, TowersInRange.lat), point(${req.params.lonParam}, ${req.params.latParam}))) AS distance, TowersInRange.radio FROM 
	(SELECT radio, lon, lat  FROM towers_${req.params.radio} WHERE st_distance_Sphere(point(lon, lat), point(${req.params.lonParam}, ${req.params.latParam})) <= towers_${req.params.radio}.range) TowersInRange
  GROUP BY radio`;

  console.log(sql)
  queryDB(sql, res);
});

function queryDB(sql, res) {
  db.query(sql, function(err, data, fields) {
    if (err) throw err;
    console.log("Erfolg")
    res.json({
      status: 200,
      data,
      message: "Cell_towers lists retrieved successfully"
    })
  })
};

module.exports = router;
