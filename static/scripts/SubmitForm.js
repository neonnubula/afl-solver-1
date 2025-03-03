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
            $.ajax({
                type: "GET",
                url: '/error',
                dataType: "html",
                success: function (result) {
                    $('#MainContent').html(result);
                },
            });
        }
    });
}
