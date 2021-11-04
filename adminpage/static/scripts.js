const getUmkms = () => {
  $.get("/admin-page/umkm-api/").done((data) => {
    let html = "";
    // data = list of todo
  
    for (let i = 0; i < data.length; i++) {
      html += `
      <tr>
        <th scope="row">${i + 1}</th>
        <td>${data[i].fields.merek_bisnis}</td>
        <td>${data[i].fields.domisili}</td>
        <td>${data[i].fields.produk_jasa}</td>
        <td class="d-flex justify-content-center align-items-center">`;
        
      if (data[i].fields.status == false){
        html += `
        <a href="/admin-page/validate/${data[i].pk}">
          <button class="btn btn-primary">validate</button>
        </a>
        `;
      } else {
        html += `
        <a href="/admin-page/invalidate/${data[i].pk}">
          <button class="btn btn-secondary">invalidate</button>
        </a>
        `;
      } 

      html += ` 
          <a href="/admin-page/delete-umkm/${data[i].pk}">
            <button class="btn btn-danger">delete</button>
          </a>
        </td>
      </tr>
      `;
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
      html += `
      <tr>
        <th scope="row">${i + 1}</th>
        <td>${data[i].fields.nama_depan} ${data[i].fields.nama_belakang}</td>
        <td>${data[i].fields.kotakabu}</td>
        <td class="d-flex justify-content-center align-items-center">
          <a href="/admin-page/delete-user/${data[i].pk}">
            <button class="btn btn-danger">delete</button>
          </a>
      </tr>
      `;
    }
    
    document.getElementById("user-data").innerHTML = "";
    document.getElementById("user-data").innerHTML = html;
  });
}

$(document).ready(() => getUsers())
  