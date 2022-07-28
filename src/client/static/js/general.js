// for general purpose js methods

document.onreadystatechange = function () {
    if (document.readyState !== "complete") {
        startLoading();
    } else {
        stopLoading();
    }
}

function redirect(path) {
    startLoading();
    window.location = path;
}

function enableElement(element) {
    element.classList.remove("disabled");
    element.disabled = false;
}

function disableElement(element) {
    element.classList.add("disabled");
    element.disabled = true;
}

// method for sending POST requests
window.post = function (url, data) {
    return fetch(url, {method: "POST", body: JSON.stringify(data)});
}

// method for sending PUT requests
window.put = function (url, data) {
    return fetch(url, {method: "PUT", body: JSON.stringify(data)});
}

// method for sending DELETE requests
window.del = function (url) {
    return fetch(url, {method: "DELETE"});
}

function startLoading() {
    document.querySelector("#loader-wrapper").style.display = "flex";
    document.querySelector("#loader-wrapper").style.visibility = "visible";
}

function stopLoading() {
    document.querySelector("#loader-wrapper").style.display = "none";
    document.querySelector("#loader-wrapper").style.visibility = "hidden";
    document.querySelector("body").style.visibility = "visible";
}