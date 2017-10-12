var client = algoliasearch("SCWGZ4PA3L", "b8015d39267687e1c6f000ff2f94b6b6")
var produtos = client.initIndex('lista_produto');

autocomplete('#aa-search-input', {}, [
    {
      source: autocomplete.sources.hits(produtos, { hitsPerPage: 3 }),
      // displayKey: 'descricao',
      templates: {
        header: '<div class="aa-suggestions-category">Produtos</div>',
        suggestion: function(suggestion) {
          return '<span>' +
            suggestion._highlightResult.descricao.value + '</span>';
        }
      }
    }
]);
