console.log("ss")
function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {       
        if(response.status == 200){
            console.log('here')
            window.location.href = '/'
        }
        else{
            alert(response.message)
        }
    })

}

function register(){
    var username = document.getElementById('makeUsername').value
    var password = document.getElementById('makePassword').value
    var cnfPassword = document.getElementById('cnfPassword').value
    var csrfs = document.getElementById('csrfs').value
    console.log('here')
    if (username == '' && password == '' && cnfPassword == ''){
        alert('You must enter all fields')
    }
    if (password != cnfPassword){
        alert('Password is not matching!')
    }
    var data = {

        'username' : username,
        'password' : password,
        'cnfPassword': cnfPassword
    }
    fetch('/api/register/', {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrfs,
        },
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {       
        if(response.status == 200){
            console.log('here')
            window.location.href = '/'
        }
        else{
            alert(response.message)
        }
    })
}

