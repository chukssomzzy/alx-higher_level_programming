$(document).ready(() => {
  $('INPUT#btn_translate').bind('click', () => {
    const code = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, (data, statusText) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
