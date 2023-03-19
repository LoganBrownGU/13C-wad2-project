
function handleXML(data) {
    var parser = new DOMParser();
    var doc = parser.parseFromString(data, "application/xml");

    nodes = doc.documentElement.childNodes;

    text = "";
    $('#films').text("");


    for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].childNodes[0] == undefined)
            continue;

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
    $('#filters').click(function () {
        var filter = $(this).val();
        var search = $('#search_text').val()

        $.get("/cinema/change_search_filter/", {'filter': filter, 'search':search}, function(data){handleXML(data)});
    });
});