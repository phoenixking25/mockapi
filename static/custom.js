$(document).ready(function(){
    $("#add").click(function(){
        var count = $(".added").length;
        count += 2;
        $("#insert").append(" <div class='row'><div class='input-field col s6'><input id='field' type='text' class='validate added' name='field" + count + "' required><label for='field'>Field " + count + "</label></div><div class='input-field col s6'><select name='datatype" + count + "' required class='validate'><option value='' disabled selected>Choose your option</option><option value='1'>String</option><option value='2'>Date</option><option value='3'>Object</option><option value='4'>Boolean</option><option value='5'>Number</option><option value='6'>Array</option></select><label>Datatype Select</label></div></div>");
        $(document).ready(function() {
            $('select').material_select();
        });
    });
});

$(document).ready(function() {
    $('select').material_select();
});
