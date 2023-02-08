<?php include ('dbconnect.php'); ?>

<?php

$sql = "DROP TABLE images";

if (mysqli_query($connect, $sql)) {
    echo "Table Images Dropped.<br>";
} else {
    echo "Error: " . $sql . "=>" . mysqli_error($connect);
}

mysqli_close($connect);
?>
