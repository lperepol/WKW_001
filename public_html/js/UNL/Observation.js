
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
            'url': '/files/json/unl/Observation.json',
            
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
   
    for (var x in subjectObject) {
        console.log("view-->" + x);
        ViewSel.options[ViewSel.options.length] = new Option(x,x);
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



var ViewSet = new Set();
var count = 1;
function displayImages() {
    var View = document.getElementById('View').value;
    var nid = null;
    //var view = document.getElementById('View');
    var zz = subjectObject[View];
    for (let i = 0; i < zz.length; i++) {
        displayimage = 'https://nematode.unl.edu/' + zz[i];
        nid = zz[i];
        var image = '<a class="example-image-link" href="[ReplaceImage]" data-lightbox="example-set" data-title="Click anywhere outside the image or the X to the right to close."><img class="example-image" src="[ReplaceThumbnail]" alt="" style="width: 150 px" /></a>';

        var image = '<div class="col-md-6"> <a href="[ReplaceImage]" target="_blank"> <img  src="[ReplaceImage]" alt="" style="width: 500px" /></a></div>';
                var image = '<img  src="[ReplaceImage]" alt="blank">';
        image = image.replace('[ReplaceImage]', displayimage);
        image = image.replace('[ReplaceImage]', displayimage);
        $('#displayDiv').append(image);

    }
    compareText =  count.toString() +  ') '  + 'NID: ' +  nid + '  '  + View + '<br>';
    count = count + 1;
    //$('#CompareDiv').text($('#CompareHeader').text().replace('', headerText));
    $('#CompareDiv').append(compareText);

    return false;
}
function resetImages() {
    count =1;
    location.reload();
}


