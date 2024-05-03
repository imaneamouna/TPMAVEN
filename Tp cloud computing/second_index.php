<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Table</title>
    <link rel="stylesheet" href="./styles.css">
</head>

<body>
<h2>Tp cloud computing </h2>
<div class="table-wrapper">
    <table class="fl-table">
        <?php
        // Your PHP code here
        // Establishing database connection
        $connect = mysqli_connect(
            'db',       // host name
            'php_docker',   // username
            'password', // password
            'php_docker'    // database name
        );

        // Checking connection
        if (!$connect) {
            die("Connection failed: " . mysqli_connect_error());
        }

        // Table name
        $table_name = "php_dacker_table";

        // Query to fetch data
        $query = "SELECT * FROM $table_name";

        // Executing query
        $response = mysqli_query($connect, $query);

        // Check if any data is returned
        if (mysqli_num_rows($response) > 0) {
            // Start building the display
            echo "<table border='1'>";
            echo "<tr><th>Title</th><th>Description</th><th>Date Created</th></tr>";
         
            // Loop through each row of data
            while ($row = mysqli_fetch_assoc($response)) {
                echo "<tr>";
                echo "<td>" . $row['title'] . "</td>";
                echo "<td>" . $row['description'] . "</td>";
                echo "<td>" . $row['date_created'] . "</td>";
                echo "</tr>";
            }

            // Close the table
            echo "</table>";
        } else {
            echo "No records found"; // Displayed if no data found
        }

        // Close the database connection
        mysqli_close($connect);
        ?>
    </div>
</body>

</html>