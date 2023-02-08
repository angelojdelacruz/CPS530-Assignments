			var counter = function(input) {
			document.getElementById('totalChars').innerHTML= input.value.length;
			
			var regex = /[a-zA-Z]/g;
			document.getElementById("alphaChars").innerHTML = input.value.match(regex).length;
		}
		

		
		var contactSub = function(input){
			event.preventDefault();
			
			const form = document.getElementById("contact");
			var formName = document.getElementById('username').value;
			var formAddress = document.getElementById("useraddress").value;
			var formPhone = document.getElementById("userphone").value;
			
			console.log(formName);
			console.log(formAddress);
			console.log(formPhone);
			
			if (validateform.call(validateform, formName, formAddress, formPhone)){
				document.getElementById('contact').style.display='none'
				document.getElementById('result').style.display= 'block';
				var newphone = convertPhone.call(convertPhone, formPhone);
				console.log(newphone);
				console.log(formName);
				showResult.call(showResult, formName, formAddress, newphone);
			}
			
			else{
				event.preventDefault();
			}
			
		}
		
		function validateform(valName, valAdd, valPhone) {
			//{}
				if (containsNum.call(containsNum, valName)) {
					alert("Name cannot contain any numbers!");
					event.preventDefault();
					return false;
				}
				else if (!(checkPhone.call(checkPhone, valPhone))){
					alert("Phone number not in valid format!");
					event.preventDefault();
					return false;
				}
				else{
					return true;
				}
			}
			
		
		function containsNum(string) {
			return /\d/.test(string);
		}
		
		function checkPhone(string) {
			var phoneRegex = /^([0-9]{3})[-]+([0-9]{3})[-]+([0-9]{4})$/;
			if(string.match(phoneRegex)) {
				return true;
			  }
			else {
				return false;
			}
		}
		
		
		function convertPhone(valPhone){
			valPhone = valPhone.substring(0, 3) + ')' + valPhone.substring(3);
			valPhone = '(' + valPhone;
			return valPhone;
		}
		
		function showResult(valName, valAdd, valPhone){
			
			document.getElementById("resultName").innerHTML = valName;
			document.getElementById("resultAddress").innerHTML = valAdd;
			document.getElementById("resultPhone").innerHTML = valPhone;
			
		}
		
		function addSiteForm() {
			event.preventDefault();
			var siteName = document.getElementById('siteName').value;
			var siteLink = document.getElementById('siteLink').value;
			var secLink = document.createElement('img');
				secLink.src = 'https://cdn-icons-png.flaticon.com/512/7216/7216133.png';
			var unsecLink = document.createElement('img');
				unsecLink.src = 'https://cdn-icons-png.flaticon.com/512/5690/5690960.png';
			var a = document.createElement('a');
				a.href = siteLink;
				a.id = siteName;
			var p = document.createElement('p');
				p.append(a);
				
			if (siteLink.includes("https")) {
				p.append(secLink);
			}
			else {
				p.append(unsecLink);
			}
			
			document.getElementById('linklist').append(p);
			document.getElementById(siteName).innerHTML = siteName;
			
		}
		