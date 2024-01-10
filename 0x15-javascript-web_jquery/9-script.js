$.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: 'fr' }, function (data) {
  $('DIV#hello').text(data.hello);
});
