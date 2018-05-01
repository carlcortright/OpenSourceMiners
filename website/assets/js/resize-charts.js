var CURRENT_DATA = "assets/data/Contributors_CountvsSourceRank.json"

onResize();
$( window ).resize(() => onResize() );

function onResize() {
    let container = $(".force-container");
    $('#force-graph').width(container.width());
    $('#force-graph').height(container.height());
    makeGraph(CURRENT_DATA);
}

