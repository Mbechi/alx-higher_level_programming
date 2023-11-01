// Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

// You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
// The translation of “Hello” must be displayed in the HTML tag DIV#hello
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API
// You script must work when imported from the <head> tag

$(function () {
  function searchCity () {
    $.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + $('#city_search').val() + '%22)&format=json', function (data, textStatus) {
      if (textStatus === 'success' && data.query.results !== null) {
        $('#wind_speed').text(data.query.results.channel.wind.speed);
      } else {
        $('#wind_speed').text('Invalid city');
      }
    });
  }
  $('#btn_search').click(searchCity);
  $('#city_search').keypress(function (event) {
    if (event.keyCode === 13) {
      searchCity();
    }
  });
});
