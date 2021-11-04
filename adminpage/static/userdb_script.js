const getUsers = () => {
    $.get("/adminpage/user-api/").done((data) => {
      let html = "";
      // data = list of todo
    
      for (let i = 0; i < data.length; i++) {
        html += `
        <tr>
          <th scope="row">${i + 1}</th>
          <td>${data[i].fields.nama_depan} ${data[i].fields.nama_belakang}</td>
          <td>${data[i].fields.kotakabu}</td>
          <td class="d-flex justify-content-center align-items-center">
            <a href="/adminpage/delete-user/${data[i].pk}">
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