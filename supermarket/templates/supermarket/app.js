//Initialize instantsearch.js
var search = instantsearch({
  // Replace with your own values
  appId: 'SCWGZ4PA3L',
  apiKey: 'b8015d39267687e1c6f000ff2f94b6b6', // search only API key, no ADMIN key
  indexName: 'lista_produto',
  urlSync: true
});

//Binding the search input
search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#search-input'
  })
);

//Displaying results
search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    hitsPerPage: 10,
    templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: "Não encontramos nenhum resultado para a busca <em>\"{{query}}\"</em>"
    }
  })
);
//Pagination
search.addWidget(
  instantsearch.widgets.pagination({
    container: '#pagination'
  })
);

//Start instantsearch
search.start();