// service para manejar el inicio de sesion usuarios, checa la BD y verifica si el usuario existe 
export async function getUserService() {
  const username = document.getElementById("user").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch(`http://localhost:8000/users/${username}`);

    if(!response.ok) { 
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const user = await response.json();

    if (user.username === username && user.password === password) {
      alert("Login successful");
      localStorage.setItem('loggedUser', true);
      window.location.href = '/tab1';
    } else {
      alert("Credenciales invalidas")
    }

  } catch(error) {
    console.error("Error fetching users:", error);
    throw error;
  }
}

// funcion para crear un nuevo usuario correspondiente a la pagina de register
export async function postUserService() {
  const username = document.getElementById("new-user").value;
  const password = document.getElementById("new-password").value;
  const password2 = document.getElementById("new-password2").value;

  if (password !== password2){
    alert("Las contraseñas no coinciden");
    return;
  }

  try {
    const response = await fetch('http://localhost:8000/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    });

    if(!response.ok){
      console.error("Error creating user:", response.statusText);
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const user = await response.json();
    alert("Usuario creado exitosamente");
    window.location.href = "/login"
    return user;

  } catch (error){
    console.error("Error posting user:", error);
    throw error;
  }
}