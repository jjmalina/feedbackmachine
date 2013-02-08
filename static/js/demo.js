function serialize_form($form) {
  $form.find('[name]').each(function(el, i) {
    var name = $(el).attr('name'),
        value = $(el).val();
    data[name] = value;
  });
  return data;
}

function post_comment(demo_id, text) {
  $.ajax({
    url: '/demos/' + demo_id + '/comments',
    data: { text: text },
    complete: function(resp) {
      console.log('complete', resp);
    }
  })
}

function listen_submit_comment() {
  $('#comment_submit').submit(function(e) {

    var $form = $(e.target),
        data = serialize_form($form);

    post_comment(data.demo_id, demo.text);

  });
}

$(function() {

  listen_submit_comment();

});
