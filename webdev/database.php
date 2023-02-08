<?php include ('dbconnect.php'); ?>

<?php
// creating a table with 5 fields
$sql = "CREATE TABLE images (
   imagenumber INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
   imagedesc VARCHAR(100) NOT NULL,
   imagelocation VARCHAR(100) NOT NULL,
   imagelink VARCHAR(100) NOT NULL,
   imagedate VARCHAR(100) NOT NULL)";

if (mysqli_query($connect, $sql)) {
    echo "Table created successfully.<br>";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($connect);
}

?>