function serialize_form($form) {

  var data = {};

  $form.find('[name]').each(function(i, el) {
    var name = $(el).attr('name'),
        value = $(el).val();
    data[name] = value;
  });

  return data;

}

function comment_submitted() {
  $('#comment_content').val('').blur();
  var $alert = $('#alert');
  var $text = $('#alert-text');
  $text.addClass('alert-success');
  $text.html("Thanks for submitting your comment!");
  $alert.removeClass('hide');
}

function comment_error() {
  $('#comment_content').blur();
  var $alert = $('#alert');
  var $text = $('#alert-text');
  $text.addClass('alert-error');
  $text.html("It seems there was a problem submitting your comment :(");
  $alert.removeClass('hide');
}

function post_comment(demo_id, content) {
  $.ajax({
    type: 'POST',
    url: '/json/demos/' + demo_id + '/comments/?format=json',
    data: { content: content },
    success: comment_submitted,
    error: comment_error
  })
}

function create_comment(e) {
  e.preventDefault();

  var $form = $('#comment_create'),
      data = serialize_form($form);

  post_comment(data.demo_id, data.content);
}

function listen_create_comment() {
  $('#comment_create').on('submit', create_comment);
  // $('#comment_submit').click(create_comment);
  $('#comment_submit').on('touchend', create_comment);
}

function poll_current_demo() {
  pages['/demo'].poller = setInterval(function() {
    var event_id = page_data.event_id;
    $.ajax({
      url: '/json/events/' + event_id + '/current_demo/?format=json',
      complete: function(resp) {
        var data = JSON.parse(resp.responseText);
        $('#current_demo').attr('href', '/demo/' + data.demo_id + '/');
      }
    });
  }, 5000);
}

pages['/demo'] = {
  init: function() {
    listen_create_comment();
    poll_current_demo();
  },
  cleanup: function() {
    clearInterval(this.poller);
    $('#comment_create').off('submit');
    $('#comment_submit').off('touchend');
  }
}
