
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
        'url': '/files/json/boldsystems/ToJSonGenus.json',

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
    var GenusSel = document.getElementById('Genus');

    for (var x in subjectObject) {
        console.log("view-->" + x);
        GenusSel.options[GenusSel.options.length] = new Option(x, x);
    }
});

function displayImages() {
    var Genus = document.getElementById('Genus').value;
    var nid = null
    //var view = document.getElementById('View');
    var z = subjectObject[Genus];
    for (let i = 0; i < z.length; i++) {

        displayimage = z[i][0];
        if (displayimage.length < 3) {
            continue;
        }
        var caption = z[i][1].trim();
        var copyright_institution = z[i][2].trim();
        var photographer = z[i][3].trim();
        var genus = z[i][4].trim();
        var species = z[i][5].trim();
        var indentifcation_method = z[i][6].trim();
        nid = z[i][0];
        var image = '<a class="example-image-link" href="[ReplaceImage]" data-lightbox="example-set" data-title="Click anywhere outside the image or the X to the right to close."><img class="example-image" src="[ReplaceThumbnail]" alt="" style="width: 150 px" /></a>';

        //var image = '<div class="col-md-6"> <a href="[ReplaceImage]" target="_blank"> <img  src="[ReplaceImage]" alt="" style="width: 500px" /></a></div>';
        //var image = '<img class= "straight" src="[ReplaceImage]" alt="blank">';
        //var image = '<figure class="figure">  <img src="[ReplaceImage]" class="figure-img img-fluid rounded" alt="A generic square placeholder image with rounded corners in a figure."> <figcaption class="figure-caption">A caption for the above image.</figcaption></figure>'                
        var image = '<figure class="figure">  <a href="[ReplaceImage]"><img src="[ReplaceImage]" class="figure-img img-fluid rounded" alt="Alt"></a> <figcaption class="figure-caption">[caption]</figcaption></figure>';
        var tax = genus;
        if (species !== "Some") {
            tax = species;
        }
        if (copyright_institution === photographer) {
            caption = tax + '<br>' + caption + '<br>' + photographer;
        } else {
            caption = tax + '<br>' + caption + '<br>' + copyright_institution + '<br>' + photographer + '<br>Indentification Method: ' + indentifcation_method;
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
    ViewSet.add(View);

    return false;
}
function resetImages() {
    count = 1;
    location.reload();
}


