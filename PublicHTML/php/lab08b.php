<?php 
		$rows = $_POST['rows'];
		$columns = $_POST['cols'];
		if ( (((int) $rows) < 3) or (((int) $rows) > 12) )
			echo "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'> 
					
					<div>
						<form action='lab08b.php' method='post'>
							<h2> Multiplication Table Generator </h2>
							<label for='rows' style='background-color:#e83636;'>Number of rows: </label>
							<input id='rows' name='rows' type='text' placeholder='3-12' required>
							<br>
							<label for='cols'>Number of columns: </label>
							<input id='cols' name='cols' type='text' placeholder='3-12' required>
							<br>
							<button type='submit'>Generate</button>
						</form>
						<h2> Please only enter numbers from 3 to 12! </h2>
					</div>
					</body>";
		elseif ( (((int) $columns) < 3) or (((int) $columns) > 12) )
			echo "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'> 
					
					<div>
						<form action='lab08b.php' method='post'>
							<h2> Multiplication Table Generator </h2>
							<label for='rows'>Number of rows: </label>
							<input id='rows' name='rows' type='text' placeholder='3-12' required>
							<br>
							<label for='cols' style='background-color:#e83636;'>Number of columns: </label>
							<input id='cols' name='cols' type='text' placeholder='3-12' required>
							<br>
							<button type='submit'>Generate</button>
						</form>
						<h2> Please only enter numbers from 3 to 12! </h2>
					</div>
					</body>";
		
		
		else {
			echo "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'> 
				
				<div>
					<h1> $rows x $columns Mulitplication Table </h1>
					<table border='2' align='center'>";
				
			for ($counter = 1; $counter <= ((int) $rows) ; $counter += 1)
			{
				echo "<tr>";
				for ($colcounter = 1; $colcounter <= ((int) $columns) ; $colcounter += 1)
				{
					$number = $counter * $colcounter;
					echo "<td style='padding:10px;'>$number</td>";
				}
				echo "</tr>";
			}
		echo "</table></div></body>"; }
?>