$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (helloData, status) => {
    $('div#hello').text(helloData.hello);
  });
});
