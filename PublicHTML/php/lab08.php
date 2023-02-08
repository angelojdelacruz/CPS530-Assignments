<?php
	date_default_timezone_set("America/Toronto");
	$currentTime = date("H:i:sa");
	
	$imageName = $_GET['image'];
	
	$hour = date('H');
	
	if ($imageName == 'ghost.gif') {
		$halloween = "<fig> <img src='ghost.gif' alt='ghost gif' style='float:right; max-width:15%; height:auto; opacity:0.4; filter:alpha(opacity=40);'> <figcaption style='float:left'>ghost.gif</figcaption> </fig>";
	}
	elseif ($imageName == 'vampire.gif') {
		$halloween = "<fig> <img src='vampire.gif' alt='vampire gif' style='float:right; max-width:15%; height:auto; opacity:0.4; filter:alpha(opacity=40);'> <figcaption style='float:left'>vampire.gif</figcaption> </fig>";
	}
	elseif ($imageName == 'skeleton.gif') {
		$halloween = "<fig> <img src='skeleton.gif' alt='skeleton gif' style='float:right; max-width:15%; height:auto; opacity:0.4; filter:alpha(opacity=40);'> <figcaption style='float:left'>skeleton.gif</figcaption> </fig>";
	}
	else {
		$halloween = "";
	}
	
	if (!isset($_COOKIE['count'])) {
		$cookie = 1;
		setcookie("count", $cookie);
		$visitnumber = 1;
	}
	else{
		$cookie = ++$_COOKIE['count'];
		setcookie("count", $cookie); 
		$visitnumber = $_COOKIE['count'];
	}
	
	if (($hour >= 6) and ($hour < 12))
		$timeImage = 'morningimage.jpg';
	elseif (($hour >= 12) and ($hour < 19))
		$timeImage = 'afternoonimage.jpg';
	elseif (($hour >= 19) and ($hour < 22))
		$timeImage = 'eveningimage.jpg';
	else
		$timeImage = 'nightimage.jpg';
	
	
	if (($hour >= 6) and ($hour < 12))
		$timeQuote = 'Good morning!';
	elseif (($hour >= 12) and ($hour < 19))
		$timeQuote = 'Good afternoon!';
	elseif (($hour >= 19) and ($hour < 22))
		$timeQuote = 'Good evening!';
	else
		$timeQuote = 'Good night!';
	
	if (($hour >= 6) and ($hour < 12))
		$quoteColor = '#651213';
	elseif (($hour >= 12) and ($hour < 19))
		$quoteColor = '#01601b';
	elseif (($hour >= 19) and ($hour < 22))
		$quoteColor = '#39046d';
	else
		$quoteColor = '#bcfdf5';
	
	echo "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'> 
			<div> 
				<h2> $halloween </h2>
				<h1> $currentTime </h1>
			</div>
			<div> 
				<img src='$timeImage' alt='time image' style='max-width:100%; height:auto;'>
				<h1 style='color:$quoteColor; margin-top:-420px; margin-bottom:420px; border: 6px solid #000214;'>$timeQuote</h1>
				
			</div> 
			
			<div>
				<form action='lab08b.php' method='post'>
					<h2> Multiplication Table Generator </h2>
					
					<label for='rows'>Number of rows: </label>
					<input id='rows' name='rows' type='text' placeholder='3-12' required>
					<br>
					<label for='cols'>Number of columns: </label>
					<input id='cols' name='cols' type='text' placeholder='3-12' required>
					<br>
					<button type='submit'>Generate</button>
				</form>
			</div>
			
			<div> 
				
				<fig>
					<img src='https://media.tenor.com/yRSnf6wABQ4AAAAi/pato-duck.gif'>
					<figcaption>the duck says $timeQuote</figcaption>
				</fig>
			</div>
			
			<div style='position:fixed; bottom:0; background-color:#004C9B; border: 6px solid #000214; '> <h2> You have visited this page $visitnumber times. </h2> </div>
			
			</body>"
			
			

	
	
?>