
function handleXML(data) {
    var parser = new DOMParser();
    var doc = parser.parseFromString(data, "application/xml");

    nodes = doc.documentElement.childNodes;

    text = "";
    $('#films').text("");   // empty the films div

    // loop through the films in the xml data
    for (let i = 0; i < nodes.length; i++) {
        // make sure the node isn't empty
        if (nodes[i].childNodes[0] == undefined)
            continue;

        // create new film link
        var newLine = document.createElement("a");
        newLine.innerHTML = nodes[i].childNodes[0].innerHTML; 
        newLine.href = "/cinema/reviews/" + nodes[i].childNodes[3].innerHTML;

        date = new Date(nodes[i].childNodes[2].innerHTML).toDateString().substring(4);

        $('#films').append(newLine);
        $('#films').append(" - " + nodes[i].childNodes[1].innerHTML + " - " + date);
        $('#films').append(document.createElement("br"));
    }
}

$(document).ready(function () {
    $('#filters').children().click(function () {
        var filter = $(this).val();
        var search = $('#search_text').html()
        search = search.split("\"")[1];

        $.get("/cinema/change_search_filter/", {'filter': filter, 'search': search}, function(data){handleXML(data)});
    });
});