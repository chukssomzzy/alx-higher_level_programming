$('DIV#red_header').bind('click', () => {
  if (!$('header').hasClass('red')) $('header').addClass('red');
});
