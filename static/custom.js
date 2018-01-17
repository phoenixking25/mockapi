$(document).ready(function(){
    $("#add").click(function(){
        var count = $(".added").length;
        count += 2;
        $("#insert").append(" <div class='row'><div class='input-field col s12'><input id='field' type='text' class='validate added' name='field" + count + "' required><label for='field'>Field " + count + "</label></div></div>");
    });
});

$(document).ready(function() {
    $('select').material_select();
});
