
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

    var arr = null;
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
    "collapsed"
    var val = value.replace('-image-target', '')
    var zz = keyObject[val];
    console.log("Target");
    console.log(val);
    var targetDivZId = '#' + value
    $(targetDivZId).empty();
    const genusSet = new Set();
    const obsSet = new Set();
    for (let i = 0; i < zz.length; i++) {
        console.log(zz[i]);
        displayimage = zz[i][0];
        genusSet.add(zz[i][1]);
        obsSet.add(zz[i][2]);
        //nid = zz[i];
        //var image = '<a class="example-image-link" href="[ReplaceImage]" data-lightbox="example-set" data-title="Click anywhere outside the image or the X to the right to close."><img class="example-image" src="[ReplaceThumbnail]" alt="" style="width: 150 px" /></a>';

        var image = '<img  src="[ReplaceImage]" alt="blank">';
        image = image.replace('[ReplaceImage]', displayimage);
        //image = image.replace('[ReplaceImage]', displayimage);
        //image = image.replace('[ReplaceImage]', displayimage);
        //$('#accordioncollapseOne001').append(image);
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


