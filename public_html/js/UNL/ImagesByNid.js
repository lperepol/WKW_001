
var imageCollection = null;
var currentImageKey = null;
var currentImageNum = null;
var currentImage = null;

var ImageName = null;
var ImageText = null;
var Gender = null;
var General = null;
var Descr = null;
var Detail = null;
var Magnification = null;
var Location = null;
var Host = null;
var Species = null;
var ScientificName_accepted = null;
var ScientificName = null;
var Class = null;
var Order = null;
var Family = null;
var Genus = null;
var Species = null;


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
            ImageTextSel = document.getElementById('ImageText');
            ImageNameSel = document.getElementById('ImageName');
            ImageTextSel = document.getElementById('ImageText');
            GenderSel = document.getElementById('Gender');
            GeneralSel = document.getElementById('General');
            DescrSel = document.getElementById('Descr');
            DetailSel = document.getElementById('Detail');
            MagnificationSel = document.getElementById('Magnification');
            LocationSel = document.getElementById('Location');
            HostSel = document.getElementById('Host');
            SpeciesSel = document.getElementById('Species');
            ScientificName_acceptedSel = document.getElementById('ScientificName_accepted');
            ScientificNameSel = document.getElementById('ScientificName');
            ClassSel = document.getElementById('Class');
            OrderSel = document.getElementById('Order');
            FamilySel = document.getElementById('Family');
            GenusSel = document.getElementById('Genus');
            SpeciesSel = document.getElementById('Species');
            displayUNLImage();
        }
    });
    /*********************************************************************/

    var arr = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': '/files/json/unl/ImagesByNid.json',

        'dataType': 'json',
        'success': function (data) {
            imageCollection = data;
            currentImageNum = 0
            currentImageKey = Object.keys(imageCollection)[currentImageNum];
            currentImage = currentImageKey;
            console.log('Current imagekey:\n' + currentImageKey);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert('Status: ' + textStatus);
            alert('Error: ' + errorThrown);
        }
    });

    /*
     $('#idEditMetadataForm').on('submit', function (e) {
     $.ajax({
     type: 'post',
     url: 'http://srv.lp-ubuntu.ca/api/wkw_001_api/wkw',
     data: $('#idEditMetadataForm').serialize(),
     success: function (q) {
     document.getElementById("pb").innerHTML = q;
     }
     });
     e.preventDefault();
     });
     */
    $('#idEditMetadataForm').submit(function (e) {
        e.preventDefault(); // don't submit multiple times
        this.submit(); // use the native submit method of the form element
        nextImage();
    });

});



function displayUNLImage() {

    displayimage = 'https://nematode.unl.edu/' + currentImage
    var image = '<a class="example-image-link" href="[ReplaceImage]" data-lightbox="example-set" data-title="Click anywhere outside the image or the X to the right to close."><img class="example-image" src="[ReplaceThumbnail]" alt="" style="width: 150 px" /></a>';

    var image = '<div class="col-md-6"> <a href="[ReplaceImage]" target="_blank"> <img  src="[ReplaceImage]" alt="" style="width: 500px" /></a></div>';
    image = image.replace('[ReplaceImage]', displayimage);
    image = image.replace('[ReplaceImage]', displayimage);
    $('#displayDiv').empty();
    $('#displayDiv').append(image);

    var NID = imageCollection[currentImage][0];
    ImageNameSel.value = NID;

    var ImageText = imageCollection[currentImage][1];
    ImageTextSel.value = ImageText;

    var SpeciesText = imageCollection[currentImage][16];
    SpeciesSel.value = SpeciesText;

    var GenderText = imageCollection[currentImage][2];
    GenderSel.value = GenderText;

    var DetailText = imageCollection[currentImage][5];
    DetailSel.value = DetailText;

    var MagnificationText = imageCollection[currentImage][6];
    MagnificationSel.value = MagnificationText;

    var LocationText = imageCollection[currentImage][7];
    LocationSel.value = LocationText;

    var HostText = imageCollection[currentImage][8];
    HostSel.value = HostText;

    /*
     LocationSel.value = LocationText;
     HostSel.value = HostText;
     SpeciesSel.value = SpeciesText;
     ScientificName_acceptedSel.value = ScientificName_acceptedText;
     ScientificNameSel.value = ScientificNameText;
     ClassSel.value = ClassText;
     OrderSel.value = OrderText;
     FamilySel.value = FamilyText;
     console.log('Image data:\n' + ImageText);
     */

    //currentImage = imageCollection[currentImageKey];

    return false;
}
function resetImages() {
    count = 1;
    location.reload();
}
function nextImage() {
    currentImageNum = currentImageNum + 1;
    currentImageKey = Object.keys(imageCollection)[currentImageNum];
    currentImage = currentImageKey;
    console.log('imageCollection:\n' + imageCollection);
    console.log('Current image key:\n' + currentImageKey);
    console.log('Current image :\n' + currentImage);
    displayUNLImage();
}

function previousImage() {
    currentImageNum = currentImageNum - 1;
    if (currentImageNum < 1) {
        currentImageNum = 0;
    }


    currentImageKey = Object.keys(imageCollection)[currentImageNum];
    currentImage = currentImageKey;
    console.log('imageCollection:\n' + imageCollection);
    console.log('Current image key:\n' + currentImageKey);
    console.log('Current image :\n' + currentImage);
    displayUNLImage();
}

