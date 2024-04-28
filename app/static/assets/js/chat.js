function fetch() {
    existing_val = $('#response').val();
    $('#response').val(existing_val + '\nYou: ' + $('#question').val());
    $.ajax({
        url: "/backend/chatbot/api/v1/getResponse",
        type: "GET",
        data: {
            question: $('#question').val(),
        },
        beforeSend: function() {$('#question').val('')},
        cache: false,
        success: function(reply) {
            // Response has come, parse and display
            if (reply.status.success == true)    {
                existing_val = $('#response').val();
                $('#response').val(existing_val + '\nBot: ' + reply.data.response);
            }
            else {
                existing_val = $('#response').val();
                $('#response').val(existing_val + '\nBot: ' + 'Some error occured!');
            }
            console.log("Response: ", reply );
            $('#response').scrollTop($('#response')[0].scrollHeight);
        },
        error: function(reply) {
            console.log("Errored!!! Response: ", reply );
            existing_val = $('#response').val();
            $('#response').val(existing_val + '\nBot: ' + 'Some error occured!');
            $('#response').scrollTop($('#response')[0].scrollHeight);
        },
    });
}

$(document).ready(function() {
    $('#hit').click(fetch);
    $("#question").on('keyup', function (e) {
        if (e.keyCode == 13) {
            fetch()
        }
    });
});


