$(function() {
    Sidebar.init();

    var container = $('#main-container');
    container.packery({
        columnWidth: 200,
        rowHeight: 200,
        itemSelector: '.item',
        gutter: 10
    });

    var itemElems = container.packery('getItemElements');
    // for each item element
    for ( var i=0, len = itemElems.length; i < len; i++ ) {
        var elem = itemElems[i];
        // make element draggable with Draggabilly
        var draggie = new Draggabilly( elem, {
            handle: '.handle'
        } );
        // bind Draggabilly events to Packery
        container.packery( 'bindDraggabillyEvents', draggie );
    }

});