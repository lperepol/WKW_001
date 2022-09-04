
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
        'url': '/files/json/boldsystems/OOFGS.json',

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
    var ViewSel = document.getElementById('View');
    var OrderSel = document.getElementById('Order');
    var FamilySel = document.getElementById('Family');
    var GenusSel = document.getElementById('Genus');
    var SpeciesSel = document.getElementById('Species');
    var GenderSel = document.getElementById('Gender');

    for (var x in subjectObject) {
        console.log("view-->" + x);
        ViewSel.options[ViewSel.options.length] = new Option(x, x);
    }

    ViewSel.onchange = function () {
        //empty Magification- and View and dropdowns
        GenderSel.length = 1;
        SpeciesSel.length = 1;
        GenusSel.length = 1;
        FamilySel.length = 1;
        OrderSel.length = 1;
        //display correct values
        for (var q in subjectObject[this.value]) {
            console.log("Order-->" + q);
            OrderSel.options[OrderSel.options.length] = new Option(q, q);
        }
    }
    OrderSel.onchange = function () {
        //empty Magification- and Topics- dropdowns
        GenderSel.length = 1;
        SpeciesSel.length = 1;
        GenusSel.length = 1;
        FamilySel.length = 1;
        //display correct values
        for (var r in subjectObject[ViewSel.value][this.value]) {
            FamilySel.options[FamilySel.options.length] = new Option(r, r);
        }
    }

    FamilySel.onchange = function () {
        //empty view dropdown
        SpeciesSel.length = 1;
        GenderSel.length = 1;
        GenusSel.length = 1;

        //display correct values
        for (var s in subjectObject[ViewSel.value][OrderSel.value][this.value]) {
            GenusSel.options[GenusSel.options.length] = new Option(s, s);
        }
    }

    GenusSel.onchange = function () {
        //empty view dropdown
        SpeciesSel.length = 1;
        GenderSel.length = 1;
        //display correct values
        for (var t in subjectObject[ViewSel.value][OrderSel.value][FamilySel.value][this.value]) {
            SpeciesSel.options[SpeciesSel.options.length] = new Option(t, t);
        }
    }
    SpeciesSel.onchange = function () {
        //empty view dropdown
        GenderSel.length = 1;
        //display correct values
        for (var u in  subjectObject[ViewSel.value][OrderSel.value][FamilySel.value][GenusSel.value][this.value]) {
            GenderSel.options[GenderSel.options.length] = new Option(u, u);
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
    var Species = document.getElementById('Species').value;
    var Gender = document.getElementById('Gender').value;
    var View = document.getElementById('View').value;
    var nid = null
    //var view = document.getElementById('View');
    var z = subjectObject[View][Order][Family][Genus][Species][Gender];
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
        }
        else {
            caption =  tax + '<br>' +  caption + '<br>' + copyright_institution + '<br>' + photographer + '<br>Indentification Method: ' + indentifcation_method;
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


