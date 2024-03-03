function SubmitForm(objSubmitButton, objForm) {
    $('#' + objSubmitButton.id).prop("disabled", true);
    var form = $('#' + objForm.id);
    $.ajax({
        type: "POST",
        url: form.attr('action'),
        data: form.serialize(),
        dataType: "html",
        success: function (result) {
            $('#MainContent').html(result);
        },
        error: function (request, status, error) {
            var form = $('#ShowError');
            $.ajax({
                type: "POST",
                url: '/error',
                data: form.serialize(),
                dataType: "html",
                success: function (result) {
                    $('#MainContent').html(result);
                },
            });
        }
    });
}
