
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
            'url': '/files/json/unl/Order_Observation.json',
            
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
    var OrderSel = document.getElementById('Order');
    var ObservationSel = document.getElementById('Observation');
   
    for (var x in subjectObject) {
        console.log("view-->" + x);
        OrderSel.options[OrderSel.options.length] = new Option(x,x);
    }
    
    OrderSel.onchange = function() {
        //empty Magification- and View and dropdowns
        ObservationSel.length = 1;
        //display correct values
        for (var q in subjectObject[this.value]) {
            console.log("Order-->" + q);
            ObservationSel.options[ObservationSel.options.length] = new Option(q,q);
        }
    }


});



var count = 1;
function displayImages() {
    var Order = document.getElementById('Order').value;
    var Observation = document.getElementById('Observation').value;
    var nid = null;
    //var view = document.getElementById('View');
    var zz = subjectObject[Order][Observation];
    for (let i = 0; i < zz.length; i++) {
        displayimage = 'https://nematode.unl.edu/' + zz[i];
        nid = zz[i];
        var image = '<a class="example-image-link" href="[ReplaceImage]" data-lightbox="example-set" data-title="Click anywhere outside the image or the X to the right to close."><img class="example-image" src="[ReplaceThumbnail]" alt="" style="width: 150 px" /></a>';

        //var image = '<div class="col-md-6"> <a href="[ReplaceImage]" target="_blank"> <img  src="[ReplaceImage]" alt="" style="width: 500px height:auto" /></a></div>';
        //var image = '<div class="col-md-6"> <a href="[ReplaceImage]" target="_blank"> <img  src="[ReplaceImage]" alt="" style="width: 500px height:auto" /></a></div>';
        var image = '<img  src="[ReplaceImage]" alt="blank">';

        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[ReplaceImage]', displayimage);
        $('#displayDiv').append(image);

    }
    compareText =  count.toString() +  ') '  + 'NID: ' +  nid + '  '  + Order +  '&#8594;' +  Observation + '<br>';
    count = count + 1;
    //$('#CompareDiv').text($('#CompareHeader').text().replace('', headerText));
    $('#CompareDiv').append(compareText);

    return false;
}
function resetImages() {
    count =1;
    location.reload();
}


