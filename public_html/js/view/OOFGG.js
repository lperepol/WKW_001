
var subjectObject = null;
$(document).ready(function() {
    /*********************************************************************/
    $.ajaxSetup({
        beforeSend: function() {
            // show gif here, eg:
            //$('#loading').show();
            $('body').addClass('loading');
        },
        complete: function() {// hide gif here, eg:
            $('body').removeClass('loading');
        }
    });
    /*********************************************************************/

        var arr = null;
        $.ajax({
            'async': false,
            'global': false,
            'url': '/files/json/view/OOFGG.json',
            
            'dataType': 'json',
            'success': function (data) {
                subjectObject = data;
                console.log(subjectObject);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert('Status: ' + textStatus); alert('Error: ' + errorThrown);
            }
        });
    /*********************************************************************/
    /*********************************************************************/
    var ViewSel = document.getElementById('View');
    var OrderSel = document.getElementById('Order');
    var FamilySel = document.getElementById('Family');
    var GenusSel = document.getElementById('Genus');
    var GenderSel = document.getElementById('Gender');
   
    for (var x in subjectObject) {
        console.log("view-->" + x);
        ViewSel.options[ViewSel.options.length] = new Option(x,x);
    }

    ViewSel.onchange = function() {
        //empty Magification- and View and dropdowns
        GenderSel.length = 1;
        GenusSel.length = 1;
        FamilySel.length = 1;
        OrderSel.length = 1;
        //display correct values
        for (var q in subjectObject[this.value]) {
            console.log("Order-->" + q);
            OrderSel.options[OrderSel.options.length] = new Option(q,q);
        }
    }
    OrderSel.onchange = function() {
        //empty Magification- and Topics- dropdowns
        GenderSel.length = 1;
        GenusSel.length = 1;
        FamilySel.length = 1;
        //display correct values
        for (var r in subjectObject[ViewSel.value][this.value]) {
            FamilySel.options[FamilySel.options.length] = new Option(r,r);
        }
    }

    FamilySel.onchange = function() {
        //empty view dropdown
        GenderSel.length = 1;
        GenusSel.length = 1;

        //display correct values
        for (var s in subjectObject[ViewSel.value][OrderSel.value][this.value]) {
            GenusSel.options[GenusSel.options.length] = new Option(s,s);
        }
    }

    GenusSel.onchange = function() {
        //empty view dropdown
        GenderSel.length = 1;
        //display correct values
        for (var t in subjectObject[ViewSel.value][OrderSel.value][FamilySel.value][this.value]) {
            GenderSel.options[GenderSel.options.length] = new Option(t,t);
        }
    }

    /* List
   var z = subjectObject[ViewSel.value][FamilySel.value][this.value];
   console.log('Am Here');
   console.log(z.length);
   for (var i = 0; i < z.length; i++) {
   console.log(z[i]);

   viewSel.options[viewSel.options.length] = new Option(z[i],z[i]);
   }
   */


});



var OrderSet = new Set();
var FamilySet = new Set();
var GenusSet = new Set();
var ViewSet = new Set();
var count = 1;
function displayImages() {
    var Order = document.getElementById('Order').value;
    var Family = document.getElementById('Family').value;
    var Genus = document.getElementById('Genus').value;
    var Gender = document.getElementById('Gender').value;
    var View = document.getElementById('View').value;
    var nid = null
    //var view = document.getElementById('View');
    var zz = subjectObject[View][Order][Family][Genus][Gender];
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
          caption = '<b>Image Index:</b> '+ image_index + '<br><b>Name:</b> ' + name + '<br>' + caption + '<br><b>Copyright Institution:</b> ' + copyright_institution + '<br><b>Photographer:</b> ' + photographer + '<br><b>Indentification Method:</b> ' + identification_method + '<br><b>Citation:</b> ' + citation;
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
        $('#displayDiv').append(image);

    }
    compareText = count.toString() + ') ' + 'NID: ' + nid + '<br> ' + Order + '&#8594;' + Family + '&#8594;' + Genus + '&#8594;' + View + '<br>';
    count = count + 1;
    //$('#CompareDiv').text($('#CompareHeader').text().replace('', headerText));
    $('#CompareDiv').append(compareText);

    return false;
}

function resetImages() {
    count =1;
    location.reload();
}


