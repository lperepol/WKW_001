
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
        'url': '/files/json/wkw/NDMFG.json',

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
    var ObservationSel = document.getElementById('Observation');
    var MagnificationSel = document.getElementById('Magnification');
    var FamilySel = document.getElementById('Family');
    var GenusSel = document.getElementById('Genus');
    var NIDSel = document.getElementById('NID');

    for (var x in subjectObject) {
        ObservationSel.options[ObservationSel.options.length] = new Option(x, x);
    }

    ObservationSel.onchange = function () {
        //empty Magification- and Topics- dropdowns
        MagnificationSel.length =1;
        FamilySel.length = 1;
        GenusSel.length = 1;
        NIDSel.length = 1;
        //display correct values
        for (var r in subjectObject[this.value]) {
            MagnificationSel.options[MagnificationSel.options.length] = new Option(r, r);
        }
    }

    MagnificationSel.onchange = function () {
        //empty Magification- and Topics- dropdowns
        FamilySel.length = 1;
        GenusSel.length = 1;
        NIDSel.length = 1;
        //display correct values
        for (var r in subjectObject[ObservationSel.value][this.value]) {
            FamilySel.options[FamilySel.options.length] = new Option(r, r);
        }
    }

    FamilySel.onchange = function () {
        //empty view dropdown
        GenusSel.length = 1;
        NIDSel.length = 1;

        //display correct values
        for (var r in subjectObject[ObservationSel.value][MagnificationSel.value][this.value]) {
            GenusSel.options[GenusSel.options.length] = new Option(r, r);
        }
    }

    GenusSel.onchange = function () {
        //empty view dropdown
        NIDSel.length = 1;
        //display correct values
        for (var r in subjectObject[ObservationSel.value][MagnificationSel.value][FamilySel.value][this.value]) {
            NIDSel.options[NIDSel.options.length] = new Option(r, r);
        }
    }

    /* List
     var z = subjectObject[NIDSel.value][MagnificationSel.value][this.value];
     console.log('Am Here');
     console.log(z.length);
     for (var i = 0; i < z.length; i++) {
     console.log(z[i]);
     
     viewSel.options[viewSel.options.length] = new Option(z[i],z[i]);
     }
     */


});



var count = 1;
function displayImages() {
    var NID = document.getElementById('NID').value;
    var Observation = document.getElementById('Observation').value;
    var Magnification = document.getElementById('Magnification').value;
    var Family = document.getElementById('Family').value;
    var Genus = document.getElementById('Genus').value;
    
    var z = subjectObject[Observation][Magnification][Family][Genus][NID];
    for (let i = 0; i < z.length; i++) {
        displayimage = z[i];

        //var image = '<div class="col-md-6"> <a href="[ReplaceImage]?raw=true" target="_blank"> <img  src="[ReplaceImage]?raw=true" alt=""  width="580" ></a></div>';
        var image = '<div class="col-md-12"> <a href="[ReplaceImage]?raw=true" target="_blank"> <img  src="[ReplaceImage]?raw=true" alt=""  width="1170" ></a></div>';
        image = image + '<div><p/>&nbsp;<br></p></div>';
        //var image = '<div > <a href="[ReplaceImage]" target="_blank"> <img  src="[ReplaceImage]?raw=true" alt=""/></a></div>';
        
        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[ReplaceImage]', displayimage);
        console.log("image");
        console.log(image);
        $('#displayDiv').append(image);

    }
    compareText =  count.toString() +  ') '  + 'NID: ' +  NID + '  ' +  Observation + '&#8594;' + Magnification + '&#8594;' + Family + '&#8594;' + Genus + '<br>';
    count = count + 1;
    $('#CompareDiv').append(compareText);

    return false;
}
function resetImages() {
    count = 1;
    location.reload();
}


