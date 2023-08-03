$(document).ready(() => {
  $('INPUT#btn_translate').bind('click', () => {
    fetchEdit();
  });
  $(document).on('keyup', (e) => {
    if (e.which === 13) { fetchEdit(); }
  });
  const fetchEdit = () => {
    const code = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, (data, statusText) => {
      $('DIV#hello').text(data.hello);
    });
  };
});
