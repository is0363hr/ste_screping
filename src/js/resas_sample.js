const fetch = require('node-fetch');


var config = require('../../config/resas_config.json')
// console.log(config);


/* 都道府県一覧 */
function prefectures(config){
  fetch(config['url'] + 'prefectures', {
    method: "GET",
    headers: { 'X-API-KEY': config['X-API-KEY']},
  }).then(response => response.json())
  .then(data => {
    console.log(data);
  });
}

/* 年代別人口 */
function population(config){
  const params = {
    prefCode: '11',
    cityCode: '11362',
    addArea: '',
  };

  const query_params = new URLSearchParams(params);

  fetch(config['url'] + 'population/composition/perYear?' + query_params, {
    method: "GET",
    headers: { 'X-API-KEY': config['X-API-KEY']},
  }).then(response => response.json())
  .then(data => {
    console.log(JSON.stringify(data));
  });
}


// prefectures(config)
population(config)