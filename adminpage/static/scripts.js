const getUmkms = () => {
  $.get("/admin-page/umkm-api/").done((data) => {
    let html = "";
    // data = list of todo
  
    for (let i = 0; i < data.length; i++) {
      html += ``;
    }
    
    document.getElementById("umkm-data").innerHTML = "";
    document.getElementById("umkm-data").innerHTML = html;
  });
}

$(document).ready(() => getUmkms())

const getUsers = () => {
  $.get("/admin-page/user-api/").done((data) => {
    let html = "";
    // data = list of todo
  
    for (let i = 0; i < data.length; i++) {
      html += ``;
    }
    
    document.getElementById("user-data").innerHTML = "";
    document.getElementById("user-data").innerHTML = html;
  });
}

$(document).ready(() => getUsers())
  