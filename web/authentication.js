function validateLogin() {
    let usernameInput = document.querySelector('input[name="username"]');
    let passwordInput = document.querySelector('input[name="password"]');
  
    let username = usernameInput.value;
    let password = passwordInput.value;
  
    if (username.length < 5 || username.length > 20) {
      alert("Имя пользователя должно быть от 5 до 20 символов.");
      usernameInput.focus(); 
      return; 
    }
  
    else if (password.length < 8 || password.length > 30) {
      alert("Пароль должен быть от 8 до 30 символов.");
      passwordInput.focus(); 
      return; 
    }
    else{
      window.location.href="search.html";
    }
  
}

function validateRegist() {
  let usernameInput = document.querySelector('input[name="username"]');
  let passwordInput = document.querySelector('input[name="password"]');

  let username = usernameInput.value;
  let password = passwordInput.value;

  if (username.length < 5 || username.length > 20) {
    alert("Имя пользователя должно быть от 5 до 20 символов.");
    usernameInput.focus(); 
    return; 
  }

  else if (password.length < 8 || password.length > 30) {
    alert("Пароль должен быть от 8 до 30 символов.");
    passwordInput.focus(); 
    return; 
  }

  else{
    window.location.href="entry.html";
  }

}