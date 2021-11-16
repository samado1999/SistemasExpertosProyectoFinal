gender = '';
age = 0.0;
pas = 0.0;
checkboxes = new Object();
checkboxesChecked = new Map();

// consume post rest service
function postData() {
    if (validData()) {
        var url = "http://127.0.0.1:8000/disease/";

        // iterate checkboxes values
        for (var [key, value] of checkboxesChecked) {
            console.log(key + ": " + value);
        }

        var data = {
            "gender": gender,
            "age": age,
            "pas_no_trat": pas,
            "pas_trat": checkboxesChecked.get('pas_trat'),
            "diabetes": checkboxesChecked.get('diabetes'),
            "smoking_status": checkboxesChecked.get('smoking_status'),
            "ecv": checkboxesChecked.get('ecv'),
            "fa": checkboxesChecked.get('fa'),
            "hvi": checkboxesChecked.get('hvi')
        };
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 201) {
                var json = JSON.parse(xhr.responseText);
                console.log(json);
                // show modal with result
                // Get the modal
                var modal = document.getElementById("myModal");

                // Get the <span> element that closes the modal
                var span = document.getElementsByClassName("close")[0];

                // When the user clicks the button, open the modal 
                modal.style.display = "block";
                // show result
                var textToModal = json.description + '\n\n' + json.symptoms + '\n\n' + json.treatment;
                document.getElementById("result").innerHTML = textToModal;

                // When the user clicks on <span> (x), close the modal
                span.onclick = function () {
                    modal.style.display = "none";
                }

                // When the user clicks anywhere outside of the modal, close it
                window.onclick = function (event) {
                    if (event.target == modal) {
                        modal.style.display = "none";
                    }
                }
            } else if (xhr.readyState === 4 && xhr.status !== 201) {
                console.log("Error: " + xhr.status);
            }
        };
        xhr.send(JSON.stringify(data));
    } else {
        alert("Por favor, llene todos los campos correctamente.");
    }
}

function validData() {
    gender = document.getElementById("gender").value;
    age = document.getElementById("age").value != '' ? parseFloat(document.getElementById("age").value) : 0;
    pas = document.getElementById("pas").value != '' ? parseFloat(document.getElementById("pas").value) : 0;
    checkboxes = document.getElementsByName("checkbox");

    // get checkboxes values
    for (var i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            checkboxesChecked.set(checkboxes[i].id, checkboxes[i].value);
        } else {
            checkboxesChecked.set(checkboxes[i].id, 0);
        }
    }

    // valid if input is not empty
    return age > 0 ? true : false;
}
