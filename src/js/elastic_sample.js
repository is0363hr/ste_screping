const eb = require('es-builder');
const elasticsearch = require('elasticsearch');

const client = new elasticsearch.Client({
  host: 'localhost:9200'
  // log: 'trace'
});

const query = eb.QueryBuilder()
  .query(eb.TermQuery('name', '承太郎'))
  .query(eb.MatchQuery('description', 'やれやれだぜ'))
  .queryMustNot(eb.TermQuery('location', '杜王町'));


JSON.stringify(query);


client.search({
  index: 'user',
  type: 'stand_user',
  body: {
    query: query
  }
}, function(err, resp) {
  // result of the search here

});