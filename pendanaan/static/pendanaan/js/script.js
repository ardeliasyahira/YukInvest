const addTodoAsync = () => {
  let data = {};
  data["csrfmiddlewaretoken"] = $("input[name=csrfmiddlewaretoken]").val();
  data["deadline"] = $("#input-deadline").val();
  data["text"] = $("#input-text").val();
  console.log(data);

  $.post("/todo/add/", data, () => getTodos());
};

const getTodos = () => {
  $.get("/todo/api/").done((data) => {
    let html = "";
    // data = list of todo
  
    for (let i = 0; i < data.length; i++) {
      html += `
      <tr>
        <th scope="row">${i + 1}</th>
        <td>${data[i].fields.text}</td>
        <td>${data[i].fields.deadline}</td>
        <td class="d-flex justify-content-center align-items-center">
          <a href="/todo/delete/${data[i].pk}">
            <button class="btn btn-danger">delete</button>
          </a>
        </td>
      </tr>
      `;
    }
    
    document.getElementById("todo-data").innerHTML = "";
    document.getElementById("todo-data").innerHTML = html;
  });
}

$(document).ready(() => getTodos())
$("#update-btn").click(() => addTodoAsync());
