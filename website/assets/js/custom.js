var CURRENT_DATA = "assets/data/Contributors_CountvsSourceRank.json"

onResize();
$( window ).resize(() => onResize() );

function onResize() {
    let container = $(".force-container");
    $('#force-graph').width(container.width());
    $('#force-graph').height(container.height());
    makeGraph(CURRENT_DATA);
}

function selectData(){
    var selected = $('#projects').val();
    let path = "assets/data/"
    if (selected.length < 2){
        alert("Please select more options.")
        return ;
    }


    var firstfound = false;

    if (selected.includes("Stars Count")) {
        path = path + "Stars_Countvs";
        firstfound = true;
    }

    if (selected.includes("Fork Count")) {
        if (firstfound){
            path = path + "Forks_Count.json";
        } else {
            path = path + "Forks_Countvs";
            firstfound = true;
        }
    }

    if (selected.includes("Open Issues Count")) {
        if (firstfound){
            path = path + "Open_Issues_Count.json"
        } else {
            path = path + "Open_Issues_Countvs";
            firstfound = true;
        }
    }

    if (selected.includes("Watchers Count")) {
        if (firstfound){
            path = path + "Watchers_Count.json"
        } else {
            path = path + "Watchers_Countvs";
            firstfound = true;
        }
    }

    if (selected.includes("Contributers Count")) {
        if (firstfound){
            path = path + "Contributors_Count.json"
        } else {
            path = path + "Contributors_Countvs";
            firstfound = true;
        }
    }

    if (selected.includes("Source Rank")) {
        if (firstfound){
            path = path + "SourceRank.json"
        }
    }

    CURRENT_DATA = path;
    makeGraph(CURRENT_DATA);
}

/* 
* Limits the number of checkboxes that can be selected
*/
$(document).ready(function() {

    var last_valid_selection = null;

    $('#projects').change(function(event) {

        if ($(this).val().length > 2) {
            $(this).val(last_valid_selection);
        } else {
            last_valid_selection = $(this).val();
        }
    });
});