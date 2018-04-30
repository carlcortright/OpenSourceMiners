

onResize();
$( window ).resize(() => onResize() );

function onResize() {
    let container = $(".force-container");
    $('#force-graph').width(container.width());
    $('#force-graph').height(container.height());
    makeGraph();
}