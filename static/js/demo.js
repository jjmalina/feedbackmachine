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
    url: '/api/v1/comments/?format=json',
    data: JSON.stringify({
      demo_id: demo_id,
      content: content
    }),
    dataType: 'json',
    contentType: 'application/json',
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

$(function() {

  listen_create_comment();

});
