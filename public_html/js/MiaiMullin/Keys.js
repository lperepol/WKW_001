
var keyObject = null;
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

    $.ajax({
        'async': false,
        'global': false,
        //'url': '/files/json/unl/UNL_Keys.json',
        //'url': '/files/json/unl/UNL_Keys_update.json',
        'url': '/files/json/MiaiMullin/Keys.json',

        'dataType': 'json',
        'success': function (data) {
            keyObject = data;
            console.log(keyObject);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert('Status: ' + textStatus);
            alert('Error: ' + errorThrown);
        }
    });


});



function displayImages(value, object) {
    console.log("displayImages");
    console.log("value");
    console.log(value);
    console.log("object");
    console.log(object);
    console.log("object class className");
    console.log(object.className);
    //if object == 
    //var view = document.getElementById('View');
    var val = value.replace('-image-target', '');
    var zz = keyObject[value];
    console.log("Target");
    console.log(val);
    var targetDivZId = '#' + value;
    $(targetDivZId).empty();
    const genusSet = new Set();
    const obsSet = new Set();
    for (let i = 0; i < zz.length; i++) {
        
var image_index=zz[i][0];
var image_name=zz[i][1];
var caption=zz[i][2];
var media_descriptor=zz[i][3];
var diagnostic_descriptor=zz[i][4];
var gender=zz[i][5];
var copyright_institution=zz[i][6];
var photographer=zz[i][7];
var genus=zz[i][8];
var species=zz[i][9];
var identification_method=zz[i][10];
var source=zz[i][11];
var common_name=zz[i][12];

        console.log(zz[i]);
        displayimage = image_name;
        genusSet.add(genus);
        obsSet.add(caption);
        var image = '';
        var name = genus;
        if (species !== "Not Specified") {
            name = species;
        }

        caption = image_index + '<br>Name: ' + name + '<br>Observing: ' + caption + '<br>Copyright Institution:' + copyright_institution + '<br>Photographer:' + photographer + '<br>Indentification Method: ' + identification_method;
        if (displayimage.endsWith('.m4v'))
        {
            image = '<figure class="figure">  <video class="VCE_Class_001" controls><source src="[ReplaceImage]" type="video/mp4"></video> <figcaption class="figure-caption">[caption]</figcaption></figure>';
        } else {
            image = '<figure class="figure">  <a href="[ReplaceImage]" target="_blank" ><img  class="img_key" src="[ReplaceImage]" class="figure-img img-fluid rounded" alt="Alt" ></a> <figcaption class="figure-caption">[caption]</figcaption></figure>';
        }
        
        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[caption]', caption);
        if (displayimage.length > 3) {
            $(targetDivZId).append(image);
        }
    }
    $(targetDivZId).prepend('<\p>');
    //const str3 = Array.from(obsSet).join(', ');
    //$(targetDivZId).prepend(str3);
    //$(targetDivZId).prepend('<br>Obs: ');
    const str2 = Array.from(genusSet).sort().join(', ');
    $(targetDivZId).prepend('</strong>' +str2 + '</strong>');
    $(targetDivZId).prepend('<br><strong>Included Genera:</strong> ');
    $(targetDivZId).prepend('<p>');

    return false;
}
function resetImages() {
    count = 1;
    location.reload();
}


