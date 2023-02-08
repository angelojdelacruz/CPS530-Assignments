<?php include ('dbconnect.php'); ?>

<?php
	

	echo "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'> 
			<div>
				<h1> Database: Random Image</h1>";
				
	$number = rand(1, 13);
	$sql = "SELECT * FROM images WHERE imagenumber = '$number'";
	$sql2 = "SELECT * FROM images";
	$result = mysqli_query($connect, $sql);
	$result2 = mysqli_query($connect, $sql2);
	$maxentries = mysqli_num_rows($result2);
				
	if (mysqli_num_rows($result) > 0) {

		  while($row = mysqli_fetch_assoc($result)) {
			$num = $row['imagenumber'];
			$desc = $row['imagedesc'];
			$location = $row['imagelocation'];
			$link = $row['imagelink'];
			$date = $row['imagedate'];
			echo "<img src='$link' alt='Picture of $desc' style='max-width:75%; height:auto; border: 6px solid #FFFFFF;border-radius:20px;'>";
			echo "<p>$num. $desc, $location ($date)</p>";
		  }
		} 
	else {
		  echo "No results.";
		}
		
		echo "<p>Number of entries in database: $maxentries</p>";
		echo "</div></body>";

mysqli_close($connect);

?>