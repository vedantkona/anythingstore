$(document).ready(function () {
    $('#uploadaudioForm').on('submit', function (e) {
        e.preventDefault();

        var formData = new FormData(this);

        $.ajax({
            url: '/audionote/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                if (response.status === 'success') {
                    alert('File uploaded successfully');
                    // Handle success, such as updating UI or showing a success message
                } else {
                    alert('Error uploading file: ' + response.message);
                    // Handle error, such as displaying an error message
                }
            },
            error: function (xhr, status, error) {
                alert('An error occurred during the upload: ' + error);
                // Handle error, such as displaying an error message
            }
        });
    });
});
