
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
            'url': '/files/json/unl/OOFGGM.json',
            
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
    var MagnificationSel = document.getElementById('Magnification');
   
    for (var x in subjectObject) {
        console.log("view-->" + x);
        ViewSel.options[ViewSel.options.length] = new Option(x,x);
    }

    ViewSel.onchange = function() {
        //empty Magification- and View and dropdowns
        MagnificationSel.length = 1;
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
        MagnificationSel.length = 1;
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
        MagnificationSel.length = 1;
        GenusSel.length = 1;

        //display correct values
        for (var s in subjectObject[ViewSel.value][OrderSel.value][this.value]) {
            GenusSel.options[GenusSel.options.length] = new Option(s,s);
        }
    }

    GenusSel.onchange = function() {
        //empty view dropdown
        GenderSel.length = 1;
        MagnificationSel.length = 1;
        //display correct values
        for (var t in subjectObject[ViewSel.value][OrderSel.value][FamilySel.value][this.value]) {
            GenderSel.options[GenderSel.options.length] = new Option(t,t);
        }
    }
    GenderSel.onchange = function() {
        //empty view dropdown
        MagnificationSel.length = 1;
        //display correct values
        for (var u in  subjectObject[ViewSel.value][OrderSel.value][FamilySel.value][GenusSel.value][this.value]) {
            MagnificationSel.options[MagnificationSel.options.length] = new Option(u,u);
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
    var Magnification = document.getElementById('Magnification').value;
    var View = document.getElementById('View').value;
    var nid = null
    //var view = document.getElementById('View');
    var z = subjectObject[View][Order][Family][Genus][Gender][Magnification];
    for (let i = 0; i < z.length; i++) {
        displayimage = 'https://nematode.unl.edu/' + z[i];
        nid = z[i];
        var image = '<a class="example-image-link" href="[ReplaceImage]" data-lightbox="example-set" data-title="Click anywhere outside the image or the X to the right to close."><img class="example-image" src="[ReplaceThumbnail]" alt="" style="width: 150 px" /></a>';

        var image = '<div class="col-md-6"> <a href="[ReplaceImage]" target="_blank"> <img  src="[ReplaceImage]" alt="" style="width: 500px" /></a></div>';
               var image = '<img  src="[ReplaceImage]" alt="blank">';
        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[ReplaceImage]', displayimage);
        $('#displayDiv').append(image);

    }
    compareText =  count.toString() +  ') '  + 'NID: ' +  nid + '  ' +  Order + '&#8594;' + Family + '&#8594;' + Genus + '&#8594;' + View + '<br>';
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
    count =1;
    location.reload();
}


