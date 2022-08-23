let id_ = ""
function saveData(){
    let data = {
        "name":$("#user_name").val(),
        "number":$("#mobile_number").val()
    }
    ajax("save_data",data)
}
function edit(id, number){
    id_ = id;
    $("#user_number_edit").val(number).trigger("change")
}
function save(){
    let data = {
        "id":id_,
        "number":$("#user_number_edit").val(),
    }
    ajax("save_edited_data",data)
}

function ajax(url,data){
    $.ajax({
        url:"/"+url,
        data:data,
        type:"POST",
        dataType: "json",
        success: function(data){
            alert(data["msg"]);
            window.location.reload();
        },
        error: function(){
            alert("Error saving data")
        }
    })
}

$(document).ready( function () {
    $('#table').DataTable();
} );