$(document).ready(() => {
  $('DIV#add_item').bind('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').bind('click', () => {
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').bind('click', () => $('UL.my_list').empty());
});
