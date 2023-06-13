$(function() {
  let header = $('.header');
  let hederHeight = header.height(); // вычисляем высоту шапки

  $(window).scroll(function() {
      if ($(this).scrollTop() > 1) {
          header.addClass('header_fixed');
          $('body').css({
              'paddingTop': hederHeight + 'px' // делаем отступ у body, равный высоте шапки
          });
      } else {
          header.removeClass('header_fixed');
          $('body').css({
              'paddingTop': 0 // удаляю отступ у body, равный высоте шапки
          })
      }

      if ($(this).scrollTop() > 1) {
        header.css({
            'padding': '5px 0',
            'background': '#ffffff',
            'transition': '.3s',
            '-webkit-box-shadow': '0 5px 25px rgba(0, 0, 0, 0.15)',
            'box-shadow': '0 5px 25px rgba(0, 0, 0, 0.15)',

        });
    } else {
        header.css({
            'padding': '19.5px 0',
            'background': '#ffffff',
            'transition': '.3s',
            '-webkit-box-shadow': '0 0 0',
            'box-shadow': '0 0 0',
        });
    }
  });
});

