
var subjectObject = null;
$(document).ready(function () {
    /*********************************************************************/
    $.ajaxSetup({
        beforeSend: function () {
            // show gif here, eg:
            //$('#loading').show();
            $('body').addClass('loading');
        },
        complete: function () {// hide gif here, eg:
            $('body').removeClass('loading');
        }
    });
    /*********************************************************************/

    var arr = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': '/files/json/view/OFG.json',

        'dataType': 'json',
        'success': function (data) {
            subjectObject = data;
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert('Status: ' + textStatus);
            alert('Error: ' + errorThrown);
        }
    });
    /*********************************************************************/
    /*********************************************************************/
    var OrderSel = document.getElementById('Order');
    var FamilySel = document.getElementById('Family');
    var GenusSel = document.getElementById('Genus');

    for (var x in subjectObject) {
        OrderSel.options[OrderSel.options.length] = new Option(x, x);
    }

    OrderSel.onchange = function () {
        //empty Magification- and Topics- dropdowns
        GenusSel.length = 1;
        FamilySel.length = 1;
        //display correct values
        for (var r in subjectObject[this.value]) {
            FamilySel.options[FamilySel.options.length] = new Option(r, r);
        }
    }

    FamilySel.onchange = function () {
        //empty view dropdown
        GenusSel.length = 1;

        //display correct values
        for (var s in subjectObject[OrderSel.value][this.value]) {
            GenusSel.options[GenusSel.options.length] = new Option(s, s);
        }
    }




});



var OrderSet = new Set();
var FamilySet = new Set();
var GenusSet = new Set();
var count = 1;
function displayImages() {
    var Order = document.getElementById('Order').value;
    var Family = document.getElementById('Family').value;
    var Genus = document.getElementById('Genus').value;
    var nid = null
    //var view = document.getElementById('View');
    var zz = subjectObject[Order][Family][Genus];
    for (let i = 0; i < zz.length; i++) {

        displayimage = zz[i][1];
        if (displayimage.length < 3) {
            continue;
        }
        var image_index = zz[i][0];

        var image_name = zz[i][1].trim();
        var caption = zz[i][2].trim();
        var media_descriptor = zz[i][3].trim();
        var diagnostic_descriptor = zz[i][4].trim();
        var gender = zz[i][5].trim();
        var copyright_institution = zz[i][6].trim();
        var photographer = zz[i][7].trim();
        var genus = zz[i][8].trim();
        var species = zz[i][9].trim();
        var identification_method = zz[i][10].trim();
        var source = zz[i][11].trim();
        var common_name = zz[i][12].trim();
        var citation = zz[i][13].trim();

        nid = zz[i][0];
        var name = genus;
        if (species.length > 0) {
            if (species !== "Not Specified") {
                name = species;
            }
        }
        caption = '<figure class="figure"> <b>Image Index:</b> ' + image_index + '<br>' + caption + '</figure>';
        var image = '';
        if (displayimage.endsWith('.m4v'))
        {
            image = '<figure class="figure">  <video class="VCE_Class_001" controls><source src="[ReplaceImage]" type="video/mp4"></video> <figcaption class="figure-caption">[caption]</figcaption></figure>';
        } else {
            image = '<figure class="figure">  <a href="[ReplaceImage]" target="_blank" ><img  class="img_no_key" src="[ReplaceImage]" class="figure-img img-fluid rounded" alt="Alt" ></a> <figcaption class="figure-caption">[caption]</figcaption></figure>';
        }

        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[caption]', caption);
        var checkBoxes = '<div class="form-check">';
        checkBoxes = checkBoxes + '<input type="checkbox" name="Body" value="' + image_index + ', Body" /><label>Body</label>';
        checkBoxes = checkBoxes + '<br><input type="checkbox" name="Head Region" value="' + image_index + ', Head Region" /><label>Head Region</label>';
        checkBoxes = checkBoxes + '<br><input type="checkbox" name="Tail Region" value="' + image_index + ', Tail Region" /><label>Tail Region</label>';

        checkBoxes = checkBoxes + '<br><input type="checkbox" name="Esophageal Region " value="' + image_index + ', Esophageal Region" /><label>Esophageal Region</label>';
        checkBoxes = checkBoxes + '<br><input type="checkbox" name="Reproductive Region" value="' + image_index + ', Reproductive Region" /><label>Reproductive Region</label>';
        checkBoxes = checkBoxes + '<br><input type="checkbox" name="Lateral Field" value="' + image_index + ', Lateral Field" /><label>Lateral Field</label>';
        checkBoxes = checkBoxes + '</div>';

        $('#displayDiv').append(checkBoxes);
        $('#displayDiv').append(image);


    }
    compareText = count.toString() + ') ' + 'NID: ' + nid + '<br> ' + Order + '&#8594;' + Family + '&#8594;' + Genus + '<br>';
    count = count + 1;
    //$('#CompareDiv').text($('#CompareHeader').text().replace('', headerText));
    $('#CompareDiv').append(compareText);

    return false;
}

function resetImages() {
    count = 1;
    location.reload();
}
function postCheckboxvalues(values) {
    var xhr = new XMLHttpRequest();
    //xhr.open("POST", 'http://127.0.0.1:5000/wkw_001_api/wkw', true);
    xhr.open("POST", 'http://srv.lp-ubuntu.ca/api/wkw_001_api/wkw', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    //headers: {'Access-Control-Allow-Origin': '*'},
    xhr.setRequestHeader('Access-Control-Allow-Headers', '*');
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
    xhr.send(JSON.stringify({
        value: values
    }));

    /*
     $.ajax({
     type: 'POST',
     url: 'http://127.0.0.1:5000/api/wkw_001_api/wkw',
     url: 'http://srv.lp-ubuntu.ca/api/wkw_001_api/wkw',
     //headers: {'Access-Control-Allow-Origin': '*'},
     headers: {'X-Content-Type-Options': 'nosniff'},
     
     // headers: {  'Access-Control-Allow-Origin': 'http://srv.lp-ubuntu.ca/api/wkw_001_api/wkw' },
     //crossDomain: true,
     data: JSON.stringify({param1: "param1", param2: "param2chriwil"}),
     //        contentType: 'text/html; charset=UTF-8',
     dataType: 'jsonp',
     success: function (responseData, textStatus, jqXHR) {
     var value = responseData.someKey;
     },
     error: function (responseData, textStatus, errorThrown) {
     console.log(responseData);
     alert('POST failed.');
     }
     });
     
     $.ajax({
     method: "POST",
     type: "POST",
     url: 'http://127.0.0.1:5000/api/wkw_001_api/wkw',
     data: "goo",
     success: function (responseData, textStatus, jqXHR) {
     var value = responseData.someKey;
     },
     error: function (responseData, textStatus, errorThrown) {
     console.log(responseData);
     alert('POST failed.');
     },
     dataType: 'jsonp'
     });
     */

}


function getCheckboxvalues() {
    var values = [];
    values.length = 0;
    $("input:checkbox[type=checkbox]:checked").each(function () {
        var val = $(this).val();
        

        values.push($(this).val());
        console.log($(this).val());
        x=2;
        for (var i=0; i<100000; i++) {
            x = x*2;
        }
    });
    postCheckboxvalues(values);
    values = [];
}
