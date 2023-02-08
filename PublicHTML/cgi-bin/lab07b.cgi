#!/usr/bin/perl -wT
use CGI ':standard';
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Switch;
use File::Basename; 
$CGI::POST_MAX = 1024 * 5000; 

my $safe_filename_characters = "a-zA-Z0-9_.-"; 
my $upload_dir = "../upload"; 
my $query = new CGI; 
my $filename = $query->param("userpic"); 
if ( !$filename ) { print $query->header ( ); print "There was a problem uploading your picture (try a smaller file)."; exit; } 
my ( $name, $path, $extension ) = fileparse ( $filename, '\..*' ); 
$filename = $name . $extension; 
$filename =~ tr/ /_/; 
$filename =~ s/[^$safe_filename_characters]//g; 

if ( $filename =~ /^([$safe_filename_characters]+)$/ ) { $filename = $1; } else { die "Filename contains invalid characters"; } 
my $upload_filehandle = $query->upload("userpic"); 

open (UPLOADFILE, ">$upload_dir/$filename") or die "$!"; binmode UPLOADFILE; 
while ( <$upload_filehandle> ) { print UPLOADFILE; } 
close UPLOADFILE; 

print $query->header ( ); 


my $name = param ('username');
my $address = param ('useraddress');
my $city = param ('usercity');
my $postal = param ('userpostal');
my $province = param ('userprovince');
my $phone = param ('userphone');
my $email = param ('useremail');


switch($province) {
	case "ontario" {$province = "Ontario"}
	case "manitoba" {$province = "Manitoba"}
	case "saskatchewan" {$province = "Saskatchewan"}
	case "quebec" {$province = "Quebec"}
	case "alberta" {$province = "Alberta"}
	case "princeedwardisland" {$province = "Prince Edward Island"}
	case "britishcolumbia" {$province = "British Columbia"}
	case "newbrunswick" {$province = "New Brunswick"}
	case "novascotia" {$province = "Nova Scotia"}
	case "newfoundlandandlabrodor" {$province = "Newfoundland and Labrodor"}
	case "nunavut" {$province = "Nunavut"}
	case "yukon" {$province = "Yukon"}
	case "northwestterritories" {$province = "Northwest Territories"}
}

unless ($phone =~ m/^(\d){10}$/) 
{
	print qq(
		<!DOCTYPE html>
		<!-- https://www.cs.ryerson.ca/~a5delacr/lab07b.html -->
		<html lang=en>
		<head>
			<title>
				Customer Registration
			</title>
			<meta name="viewport" content="width=device-width, initial-scale=1">

		</head>


		<body style="background-color:#36235c; text-align:center; font-family:Verdana, sans-serif;">

		<style>
			div.infobox {
				display: block;
				background-color:#8B23E6; 
				max-width:60%;
				margin-top:2%;
				margin-left:20%;
				border: 6px solid #6e20b3;
				border-radius:20px;
				
			}
			
			div.left{
				float:center;
				
			}
			
			div.clear{
				clear:both;
			}
			
			.text {
				color:#F3D677;
				font-family:Verdana, sans-serif;
				margin-top:5px;
				text-align:center;
			}
			
			form{
				text-align:center;
			}
			
		</style>

		<div class="infobox">
			<div class="text" id="register" style="text-align:left; margin-left:2%"> <!-- Regsistration submission -->
					<form method="post" id="registerform" action = "https://www2.scs.ryerson.ca/~a5delacr/cgi-bin/lab07b.cgi" enctype="multipart/form-data">
						<h2 class="text"> Contact Submission </h2>
						<div class="left">
							<label for="username">Name: </label>
							<input id = "username" name = "username" type = "text" placeholder = "John Smith" required>
							<label for="useraddress">Address: </label>
							<input id = "useraddress" name = "useraddress" type = "text" placeholder = "3080 Chainsmith Street" required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="usercity">City: </label>
							<input id = "usercity" name = "usercity" type = "text" placeholder = "New Motostoke" required>
							<label for="userpostal">Postal Code: </label>
							<input id = "userpostal" name = "userpostal" type = "text" placeholder = "A1B 2C3" required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="userprovince">Province/Territory: </label>
							<select name="userprovince" id="userprovince">
								<optgroup label="Provinces">
									<option value="Ontario">Ontario</option>
									<option value="Manitoba">Manitoba</option>
									<option value="Saskatchewan">Saskatchewan</option>
									<option value="Quebec">Quebec</option>
									<option value="Alberta">Alberta</option>
									<option value="Prince Edward Island">Prince Edward Island</option>
									<option value="British Columbia">British Columbia</option>
									<option value="New Brunswick">New Brunswick</option>
									<option value="Nova Scotia">Nova Scotia</option>
									<option value="Newfoundland and Labrodor">Newfoundland and Labrodor</option>
								</optgroup>
								<optgroup label="Territories">
									<option value="Nunavut">Nunavut</option>
									<option value="Yukon">Yukon</option>
									<option value="Northwest Territories">Northwest Territories</option>
								</optgroup>
							</select>
							<label for="userphone" style="background-color:#e83636;">Phone Number: </label>
							<input id = "userphone" name = "userphone" type = "text" placeholder = "1234567890" required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="useremail">Email: </label>
							<input id = "useremail" name = "useremail" type = "text" placeholder = "duck.dancing\@birdmail.quack" required>
							<label for="userpic">Avatar: </label>
							<input id = "userpic" name = "userpic" type = "file" required>
						</div>
						<div class="clear">&nbsp;</div>
						<button type="submit" style="margin:5px;">Register</button>
					</form>
				</div>
		</div>
		</body>
		</html>
);
exit;
}

unless ($postal =~ m/^(\w)(\d)(\w)(\s)(\d)(\w)(\d)$/)
{
	print qq(
		<!DOCTYPE html>
		<!-- https://www.cs.ryerson.ca/~a5delacr/lab07b.html -->
		<html lang=en>
		<head>
			<title>
				Customer Registration
			</title>
			<meta name="viewport" content="width=device-width, initial-scale=1">

		</head>


		<body style="background-color:#36235c; text-align:center; font-family:Verdana, sans-serif;">

		<style>
			div.infobox {
				display: block;
				background-color:#8B23E6; 
				max-width:60%;
				margin-top:2%;
				margin-left:20%;
				border: 6px solid #6e20b3;
				border-radius:20px;
				
			}
			
			div.left{
				float:center;
				
			}
			
			div.clear{
				clear:both;
			}
			
			.text {
				color:#F3D677;
				font-family:Verdana, sans-serif;
				margin-top:5px;
				text-align:center;
			}
			
			form{
				text-align:center;
			}
			
		</style>

		<div class="infobox">
			<div class="text" id="register" style="text-align:left; margin-left:2%"> <!-- Regsistration submission -->
					<form method="post" id="registerform" action = "https://www2.scs.ryerson.ca/~a5delacr/cgi-bin/lab07b.cgi" enctype="multipart/form-data">
						<h2 class="text"> Contact Submission </h2>
						<div class="left">
							<label for="username">Name: </label>
							<input id = "username" name = "username" type = "text" placeholder = "John Smith" required>
							<label for="useraddress">Address: </label>
							<input id = "useraddress" name = "useraddress" type = "text" placeholder = "3080 Chainsmith Street" required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="usercity">City: </label>
							<input id = "usercity" name = "usercity" type = "text" placeholder = "New Motostoke" required>
							<label for="userpostal" style="background-color:#e83636;">Postal Code: </label>
							<input id = "userpostal" name = "userpostal" type = "text" placeholder = "A1B 2C3" required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="userprovince">Province/Territory: </label>
							<select name="userprovince" id="userprovince">
								<optgroup label="Provinces">
									<option value="Ontario">Ontario</option>
									<option value="Manitoba">Manitoba</option>
									<option value="Saskatchewan">Saskatchewan</option>
									<option value="Quebec">Quebec</option>
									<option value="Alberta">Alberta</option>
									<option value="Prince Edward Island">Prince Edward Island</option>
									<option value="British Columbia">British Columbia</option>
									<option value="New Brunswick">New Brunswick</option>
									<option value="Nova Scotia">Nova Scotia</option>
									<option value="Newfoundland and Labrodor">Newfoundland and Labrodor</option>
								</optgroup>
								<optgroup label="Territories">
									<option value="Nunavut">Nunavut</option>
									<option value="Yukon">Yukon</option>
									<option value="Northwest Territories">Northwest Territories</option>
								</optgroup>
							</select>
							<label for="userphone">Phone Number: </label>
							<input id = "userphone" name = "userphone" type = "text" placeholder = "1234567890"  required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="useremail">Email: </label>
							<input id = "useremail" name = "useremail" type = "text" placeholder = "duck.dancing\@birdmail.quack" required>
							<label for="userpic">Avatar: </label>
							<input id = "userpic" name = "userpic" type = "file" required>
						</div>
						<div class="clear">&nbsp;</div>
						<button type="submit" style="margin:5px;">Register</button>
					</form>
				</div>
		</div>
		</body>
		</html>
);
exit;
}

unless ($email =~ m/^.+@.+(\.).+$/)
{
	print qq(
		<!DOCTYPE html>
		<!-- https://www.cs.ryerson.ca/~a5delacr/lab07b.html -->
		<html lang=en>
		<head>
			<title>
				Customer Registration
			</title>
			<meta name="viewport" content="width=device-width, initial-scale=1">

		</head>


		<body style="background-color:#36235c; text-align:center; font-family:Verdana, sans-serif;">

		<style>
			div.infobox {
				display: block;
				background-color:#8B23E6; 
				max-width:60%;
				margin-top:2%;
				margin-left:20%;
				border: 6px solid #6e20b3;
				border-radius:20px;
				
			}
			
			div.left{
				float:center;
				
			}
			
			div.clear{
				clear:both;
			}
			
			.text {
				color:#F3D677;
				font-family:Verdana, sans-serif;
				margin-top:5px;
				text-align:center;
			}
			
			form{
				text-align:center;
			}
			
		</style>

		<div class="infobox">
			<div class="text" id="register" style="text-align:left; margin-left:2%"> <!-- Regsistration submission -->
					<form method="post" id="registerform" action = "https://www2.scs.ryerson.ca/~a5delacr/cgi-bin/lab07b.cgi" enctype="multipart/form-data">
						<h2 class="text"> Contact Submission </h2>
						<div class="left">
							<label for="username">Name: </label>
							<input name = "username" type = "text" placeholder = "John Smith" required>
							<label for="useraddress">Address: </label>
							<input id = "useraddress" name = "useraddress" type = "text" placeholder = "3080 Chainsmith Street" required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="usercity">City: </label>
							<input id = "usercity" name = "usercity" type = "text" placeholder = "New Motostoke" required>
							<label for="userpostal">Postal Code: </label>
							<input id = "userpostal" name = "userpostal" type = "text" placeholder = "A1B 2C3" required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="userprovince">Province/Territory: </label>
							<select name="userprovince" id="userprovince">
								<optgroup label="Provinces">
									<option value="Ontario">Ontario</option>
									<option value="Manitoba">Manitoba</option>
									<option value="Saskatchewan">Saskatchewan</option>
									<option value="Quebec">Quebec</option>
									<option value="Alberta">Alberta</option>
									<option value="Prince Edward Island">Prince Edward Island</option>
									<option value="British Columbia">British Columbia</option>
									<option value="New Brunswick">New Brunswick</option>
									<option value="Nova Scotia">Nova Scotia</option>
									<option value="Newfoundland and Labrodor">Newfoundland and Labrodor</option>
								</optgroup>
								<optgroup label="Territories">
									<option value="Nunavut">Nunavut</option>
									<option value="Yukon">Yukon</option>
									<option value="Northwest Territories">Northwest Territories</option>
								</optgroup>
							</select>
							<label for="userphone">Phone Number: </label>
							<input id = "userphone" name = "userphone" type = "text" placeholder = "1234567890"  required>
						</div>
						<div class="clear">&nbsp;</div>
						<div class="left">
							<label for="useremail" style="background-color:#e83636;">Email: </label>
							<input id = "useremail" name = "useremail" type = "text" placeholder = "duck.dancing\@birdmail.quack" required>
							<label for="userpic">Avatar: </label>
							<input id = "userpic" name = "userpic" type = "file" required>
						</div>
						<div class="clear">&nbsp;</div>
						<button type="submit" style="margin:5px;">Register</button>
					</form>
				</div>
		</div>
		</body>
		</html>
);
exit;
}



print qq(
	<!DOCTYPE html>
	<!-- https://www.cs.ryerson.ca/~a5delacr/lab07b.html -->
	<html lang=en>
	<head>
		<title>
			Customer Registration
		</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">

	</head>


	<body style="background-color:#36235c; text-align:center; font-family:Verdana, sans-serif;">

	<style>
		div.infobox {
			display: block;
			background-color:#8B23E6; 
			max-width:60%;
			margin-top:2%;
			margin-left:20%;
			border: 6px solid #6e20b3;
			border-radius:20px;
			
		}
		
		div.left{
			float:center;
			
		}
		
		div.clear{
			clear:both;
		}
		
		.text {
			color:#F3D677;
			font-family:Verdana, sans-serif;
			margin-top:5px;
			text-align:center;
		}
		
		
	</style>

	<div class="infobox">
		<div class="text" id="register" style="text-align:left; margin-left:2%"> <!-- Regsistration submission -->
				<h2 class=text> Thank you for registering! A confirmation email will be sent shortly. </h2>
				<p>Name: $name</p>
				<p>Address: $address</p>
				<p>City: $city</p>
				<p>Postal code: $postal</p>
				<p>Province/Territory: $province</p>
				<p>Phone number: $phone</p>
				<p>Email: $email</p>
				<p>Submitted profile picture:</p>
				<p><img src="../upload/$filename" alt="Uploaded picture" style="background-color:8B23E6;border: 6px solid #6e20b3; border-radius:10px;"/></p>
			</div>
	</div>
	
	<fig>
		<img src="https://media.tenor.com/yRSnf6wABQ4AAAAi/pato-duck.gif">
		<figcaption>the duck is happy with your submission</figcaption>
	</fig>
	
	</body>
	</html>
);