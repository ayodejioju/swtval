const axios = require("axios");

async function callPythonAPI() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/");
        console.log("Python API says:", response.data);

        const user = await axios.get("http://127.0.0.1:8000/users/5");
        console.log("User:", user.data);
    } catch (error) {
        console.error("Error calling API:", error.message);
    }
}

callPythonAPI();
