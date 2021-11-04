const getUmkms = () => {
  $.get("/adminpage/umkm-api/").done((data) => {
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
        <a href="/adminpage/validate/${data[i].pk}">
          <button class="btn btn-primary">validate</button>
        </a>
        `;
      } else if (data[i].fields.status == true){
        html += `
        <a href="/adminpage/invalidate/${data[i].pk}">
          <button class="btn btn-secondary">invalidate</button>
        </a>
        `;
      } 

      html += ` 
          <a href="/adminpage/delete-umkm/${data[i].pk}">
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