/**
 * Used to send a request.
 *
 * @param String url
 * @param String type - type of request, such as GET, POST, PUT, etc...
 * @param Object data
 * @param function callback(response)
 */
function request(url, type, data, callback) {
    var xhr = new XMLHttpRequest();
    
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE)
            callback(xhr.responseText);
    }
    
    xhr.open(type.toUpperCase(), url, true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(data));
};

