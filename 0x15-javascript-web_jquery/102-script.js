$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';

  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    console.log('Language Code:', languageCode);

    $.get(`${url}lang=${languageCode}`, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
