document.addEventListener('DOMContentLoaded', () => {
  const divElem = document.querySelector('DIV#red_header');
  const headerElem = document.querySelector('header');
  const changeHeaderColor = () => (headerElem.style.color = '#ff0000');

  if (divElem) divElem.addEventListener('click', changeHeaderColor);
});
