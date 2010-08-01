
var add_topic_to_list = function(topic_list, topic) {
    var topic_id = topic["topic_id"];
    var topic_url = topic["url"];
    var has_voted = topic["has_voted"];
    var volunteer_url = topic["volunteer_url"];
    var presenter = topic["has_presenter"];
    var list_item = "<li>"
    list_item += "<div class=\"container_10 clearfix\">"
    list_item += "<div class=\"grid_2\">"
    list_item += "<p class=\"vote_count\" id=\"vote_count_" + topic_id + "\">" + topic["votes"] + "</p>\n"
    if(has_voted) {
	list_item += "<p class=\"voted\">Voted</p>" 
    }
    else{
    list_item += "<p><a class=\"vote_up\" id=\"vote_up_" + topic_id + "\">Vote</a></p>" 
    }
    list_item += "</div><div class=\"grid_6\">"
    list_item += "<a href=\"" + topic_url + "\">" + topic["title"] + "</a>";
    list_item += "</p><div class=\"description\">" + topic["description"];
    list_item += "</div>\n";
    list_item += "<p><div class=\"byline\">Suggested by " + topic["creator"];

    if(presenter) {
	list_item += " <span class=\"presenter\">(Has presenter)</span>";
    }
    else {
	list_item += " <span class=\"presenter\">(No presenter - volunteer!)</span>";
    }
    list_item += "</div></div></div>\n";


    list_item +=  "</li>\n";
    topic_list.append(list_item);
}

var set_topic_list = function(topic_data, tag) {
    var topic_list = $(tag);
    if(topic_data.length == 0) {
	topic_list.html("");
	var title = $("#title")
	$("#search_results").hide();
	$("#notopics").show();
    }
    else {
	$("#notopics").hide();
	$("#search_results").show();
	topic_list.hide()
	topic_list.html("");
	for(var i = 0; i < topic_data.length; i++) {
	    add_topic_to_list(topic_list, topic_data[i]);
	}
	topic_list.show();
    }
}
