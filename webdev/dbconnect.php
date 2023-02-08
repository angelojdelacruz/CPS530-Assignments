<?php
$host = "localhost";
$database = "a5delacr";
$user = "a5delacr";
$password = "Evit7Dis";

$connect = mysqli_connect($host, $user, $password, $database) 
or die(mysqli_error());
echo "<div>Connected to MySQL Database <b>$database</b></div>";
?>