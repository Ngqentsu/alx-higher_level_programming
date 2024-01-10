$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';

  $('INPUT#btn_translate').click(translate);

  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        $.get(`${url}lang=${$('INPUT#language_code').val()}`, function (data) {
          $('DIV#hello').html(data.hello);
        });
      }
    });
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(`${url}lang=${$('INPUT#language_code').val()}`, function (data) {
    $('DIV#hello').html(data.hello);
  });
}
