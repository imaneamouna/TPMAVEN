<?php
session_start();

// Database connection details
$servername = "localhost";
$username = "root";
$password = "";
$database = "your_database_name";


// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the posted username and password
$username = $_POST['username'];
$password = $_POST['password'];

// Prepare SQL statement to fetch user credentials
$stmt = $conn->prepare("SELECT username, password FROM users WHERE username = ?");
$stmt->bind_param("s", $username);
$stmt->execute();
$result = $stmt->get_result();

// Check if a row is returned
if ($result->num_rows == 1) {
    // Fetch row
    $row = $result->fetch_assoc();

    // Verify password
    if (password_verify($password, $row['password'])) {
        // Authentication successful
        $_SESSION['username'] = $username;
        header("Location: dashboard.php"); // Redirect to dashboard or any other page
        exit();
    } else {
        // Authentication failed
        echo "Invalid username or password. Please try again.";
    }
} else {
    // User not found
    echo "Invalid username or password. Please try again.";
}

// Close statement and connection
$stmt->close();
$conn->close();
?>
