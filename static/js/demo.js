function serialize_form($form) {

  var data = {};

  $form.find('[name]').each(function(i, el) {
    var name = $(el).attr('name'),
        value = $(el).val();
    data[name] = value;
  });

  return data;

}

function post_comment(demo_id, content) {
  $.ajax({
    type: 'POST',
    url: '/json/demos/' + demo_id + '/comments/?format=json',
    data: { content: content },
    complete: function(resp) {
      console.log('complete', resp);
    }
  })
}

function create_comment(e) {
  e.preventDefault();

  var $form = $('#comment_create'),
      data = serialize_form($form);

  post_comment(data.demo_id, data.content);
}

function listen_create_comment() {
  $('#comment_create').submit(create_comment);
  // $('#comment_submit').click(create_comment);
  $('#comment_submit').on('touchend', create_comment);
}

function poll_current_demo() {
  setInterval(function() {
    var event_id = bootstrap.event_id;
    $.ajax({
      url: '/json/events/' + event_id + '/current_demo/?format=json',
      complete: function(resp) {
        var data = JSON.parse(resp.responseText);
        $('#current_demo').attr('href', '/demo/' + data.demo_id + '/');
      }
    });
  }, 5000);
}

$(function() {

  listen_create_comment();
  poll_current_demo();

});
