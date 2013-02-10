var page_data = {};

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

function update_current_demo_link(demo_id) {
  var $current_demo = $('#current_demo');
  var on_current_demo = (demo_id == page_data.demo_id);
  $current_demo.attr('href', '/demo/' + demo_id + '/');
  $current_demo.toggleClass('hide', on_current_demo);
}

function poll_current_demo() {
  update_current_demo_link(page_data.current_demo_id);
  pages['/demo'].poller = setInterval(function() {
    var event_id = page_data.event_id;
    $.ajax({
      url: '/json/events/' + event_id + '/current_demo/?format=json',
      complete: function(resp) {
        var data = JSON.parse(resp.responseText);
        update_current_demo_link(data.demo_id);
      }
    });
  }, 5000);
}

pages['/demo'] = {
  init: function() {
    page_data = JSON.parse($('#page_data').text());
    listen_create_comment();
    poll_current_demo();
  },
  cleanup: function() {
    clearInterval(this.poller);
    $('#comment_create').off('submit');
    $('#comment_submit').off('touchend');
  }
}
