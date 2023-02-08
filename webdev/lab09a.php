
<?php include ('dbconnect.php'); ?>


<?php
$sql = "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Toronto','Ontario','pictures/toronto1.jpg','2017');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Ottawa','Ontario','pictures/ottawa.jpg','2021');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('The Thousand Islands','Ontario','pictures/thousandislands.jpg','2018');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Bruce Peninsula','Ontario','pictures/brucepeninsula.jpg','2022');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Bern','Switzerland','pictures/bern.jpg','2021');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('London','UK','pictures/london.jpg','2019');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Moscow','Russia','pictures/moscow.jpg','2017');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Groningen','Netherlands','pictures/netherlands.jpg','2021');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('New York','USA','pictures/newyork.jpg','2019');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Pachuca','Mexico','pictures/pachuca.jpg','2022');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Reykjavík','Iceland','pictures/reykyavik.jpg','2018');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Tokyo','Japan','pictures/tokyo.jpg','2016');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Shibuya','Japan','pictures/tokyo2.jpg','2017');";
$sql .= "INSERT INTO images (imagedesc, imagelocation, imagelink, imagedate)
VALUES ('Duck','.gif','pictures/duck-bwong.gif,'2022');";


if (mysqli_multi_query($connect, $sql)) {
    echo "Multiple images added.<br>";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($connect);
}

mysqli_close($connect);
?>