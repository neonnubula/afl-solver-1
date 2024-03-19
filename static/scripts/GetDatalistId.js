$.GetDatalistId = function($control_id, $hidden_field_id) {
    $hidden_field_id.val($('#' + $control_id.attr('list') + ' option[value =\'' + $control_id.val().replace('\'', '\\\'') + '\']').attr('data-value'));
}

$.GetSelectedOptionText = function ($control_id, $hidden_field_id) {
    $hidden_field_id.val($control_id.find('option:selected').text());
}
