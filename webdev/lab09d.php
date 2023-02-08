<?php include ('dbconnect.php'); ?>

<?php
	
	

	echo "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'> 
			<div>
				<h1> Database: Choose Images</h1>
			<form action='lab09d.php' method='post' id='filterform'>
			<h2> Image Filters </h2>
			<label for='dates'>Year: </label>
					<select name='dates' id='dates'>
							<option value='2022'>2022</option>
							<option value='2021'>2021</option>
							<option value='2020'>2020</option>
							<option value='2019'>2019</option>
							<option value='2018'>2018</option>
							<option value='2017'>2017</option>
							<option value='2016'>2016</option>
					</select>
			<label for='locations'>Country: </label>
					<select name='locations' id='locations'>
							<option value='Ontario'>Ontario</option>
							<option value='Japan'>Japan</option>
							<option value='Switzerland'>Switzerland</option>
							<option value='UK'>UK</option>
							<option value='Russia'>Russia</option>
							<option value='Netherlands'>Netherlands</option>
							<option value='Mexico'>Mexico</option>
							<option value='USA'>USA</option>
							<option value='Iceland'>Iceland</option>
					</select>
			
			<button type='submit'>Filter</button>
		</form>";
		
	$dates = $_POST['dates'];
	$locations = $_POST['locations'];
	
	echo "<p>Images taken in $dates from $locations</p>";
	
	$sql = "SELECT * FROM images WHERE imagelocation = '$locations' AND imagedate= '$dates'";
	$result = mysqli_query($connect, $sql);
	
	if (mysqli_num_rows($result) > 0) {

		  while($row = mysqli_fetch_assoc($result)) {
			$num = $row['imagenumber'];
			$desc = $row['imagedesc'];
			$location = $row['imagelocation'];
			$link = $row['imagelink'];
			$date = $row['imagedate'];
			echo "<img src='$link' alt='Picture of $desc' style='max-width:75%; height:auto; border: 6px solid #FFFFFF;border-radius:20px;'>";
			echo "<p>$desc, $location ($date)</p>";
		  }
		} 
	else {
		  echo "No results from selected filters.";
		}
		
		echo "</div></body>";

mysqli_close($connect);

?>