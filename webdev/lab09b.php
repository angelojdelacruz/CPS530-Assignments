<?php include ('dbconnect.php'); ?>

<?php
	$sql = "SELECT * FROM images ORDER BY imagedate DESC";
	$result = mysqli_query($connect, $sql);

	echo "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'> 
			<div>
				<h1> Database: All Images</h1>";
				
	if (mysqli_num_rows($result) > 0) {

		  while($row = mysqli_fetch_assoc($result)) {
			$num = $row['imagenumber'];
			$desc = $row['imagedesc'];
			$location = $row['imagelocation'];
			$link = $row['imagelink'];
			$date = $row['imagedate'];
			echo "<img src='$link' alt='Picture of $desc' style='max-width:75%; height:auto; border: 6px solid #FFFFFF;border-radius:20px;'>";
			echo "<p>$num. $desc, $location ($date), stored in ~/$link.</p>";
		  }
		} 
	else {
		  echo "No results.";
		}
		
		echo "</div></body>";

mysqli_close($connect);

?>