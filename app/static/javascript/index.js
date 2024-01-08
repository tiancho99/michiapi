console.log("cargado correctamente")
function fetchData() {
    // Get the input value
    console.log("hola")
    let inputData = document.getElementById('search').value;

    // Make sure input is not empty
    if (!inputData) {
        inputData = "michis/1"
    }

    console.log(inputData)
    // Construct the API URL (replace 'YOUR_API_ENDPOINT' with the actual API endpoint)
    const ARGS = "?format=json"
    let apiUrl = API_ENDPOINT + inputData + ARGS;
    console.log(apiUrl)
    // Make a GET request to the API
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // Display the fetched data in the result div
            document.getElementById('canvas-data').innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            document.getElementById('canvas-data').innerHTML = 'Error fetching data.';
        });
}