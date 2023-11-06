    function generateShareLink(questionId) {
        var baseUrl = getBaseURL();
        var shareableLink = baseUrl + 'study/share/' + questionId; // Replace '/share/' with your actual route for sharing questions

        // Create an input element to hold the shareable link temporarily
        var tempInput = document.createElement('input');
        tempInput.value = shareableLink;
        document.body.appendChild(tempInput);

        // Select the input element's content
        tempInput.select();
        tempInput.setSelectionRange(0, 99999); // For mobile devices

        // Copy the shareable link to the clipboard
        document.execCommand('copy');
        
        // Remove the temporary input element
        document.body.removeChild(tempInput);

        // Provide a visual cue or message to indicate the link has been copied

        // alert('Do you want to copy the shareable link of this question - ' + shareableLink + '?');
        alert('Copy the link?');
    }

    // Replace this with your function to retrieve the base URL of your application
    function getBaseURL() {
        // Implement the logic to get the base URL of your application
        // This might involve Django's template tags or other methods to obtain the base URL
        return 'http://127.0.0.1:8002/'; // Replace with your actual base URL
    }
