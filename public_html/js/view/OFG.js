
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
            console.log(subjectObject);
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
        console.log("view-->" + x);
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
    var z = subjectObject[Order][Family][Genus];
    for (let i = 0; i < z.length; i++) {

        displayimage = z[i][0];
        if (displayimage.length < 3) {
            continue;
        }
        var caption = z[i][1].trim();
        var gender = z[i][2].trim();
        var copyright_institution = z[i][3].trim();
        var photographer = z[i][4].trim();
        var genus = z[i][5].trim();
        var species = z[i][6].trim();
        var indentifcation_method = z[i][7].trim();
        var source = z[i][8].trim();
        nid = z[i][0];
        var name = genus;
        if (species !== "Not Specified") {
            name = species;
        }
        if (copyright_institution === photographer) {
            caption = tax + '<br>' + caption + '<br>' + photographer;
        } else {
            caption = 'Name: ' + name + '<br>' + caption + '<br>Copyright Institution:' + copyright_institution + '<br>Photographer:' + photographer + '<br>Indentification Method: ' + indentifcation_method;
        }
        var image = '';
        if (displayimage.endsWith('.m4v'))
        {
            image = '<figure class="figure">  <video class="VCE_Class_001" controls><source src="[ReplaceImage]" type="video/mp4"></video> <figcaption class="figure-caption">[caption]</figcaption></figure>';
        } else {
            image = '<figure class="figure">  <a href="[ReplaceImage]" target="_blank" ><img src="[ReplaceImage]" class="figure-img img-fluid rounded" alt="Alt" ></a> <figcaption class="figure-caption">[caption]</figcaption></figure>';
        }

        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[caption]', caption);
        $('#displayDiv').append(image);

    }
    compareText = count.toString() + ') ' + 'NID: ' + nid + '<br> ' + Order + '&#8594;' + Family + '&#8594;' + Genus + '&#8594;' + View + '<br>';
    count = count + 1;
    //$('#CompareDiv').text($('#CompareHeader').text().replace('', headerText));
    $('#CompareDiv').append(compareText);
    OrderSet.add(Order);
    FamilySet.add(Family);
    GenusSet.add(Genus);

    return false;
}

function resetImages() {
    count = 1;
    location.reload();
}


