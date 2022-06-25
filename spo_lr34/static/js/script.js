fill_data_list = function () {
    $.getJSON('/get_all_data', function (data) {
        $("#data").html("");
        $.each(data, function (i, item) {
            $("<div class = 'row'> id = '" + i + '>').html(
                "<div class='col' id='id'>" + item[0] +
                "</div><div class='col' id='value'>" + item[1] +
                "</div><div class='col' id='description'>" + item[2] +
                "</div>" +
                "<div class='col'><a href onclick='update_data(" + item[0] +
                ");return false;'>Добавить описание</a>" +
                "<a href onclick='get_links_for_term(" + item[0] +
                ");return false;'>Cвязи</a>" + "</div>"
            ).appendTo('#data');
        });
    });
}

fill_types = function () {
    $.getJSON('/get_all_types', function (data) {
        $("#all_types").html("");
        $.each(data, function (i, item) {
            $("<div class = 'row'> id = '" + i + '>').html(
                "<div class='col' id='type_id'>" + item[0] +
                "</div><div class='col' id='type_name'>" + item[1] +
                "</div><div class='col' id='source_name'>" + item[2] +
                "</div><div class='col' id='target_name'>" + item[3] +
                "</div></div>"
            ).appendTo('#all_types');
        });
    });
}

fill_links = function () {
    $.getJSON('/get_all_links', function (data) {
        $("#data_link").html("");
        $.each(data, function (i, item) {
            $("<div class = 'row'> id = '" + i + '>').html(
                "<div class='col' id='link_id'>" + item[0] +
                "</div><div class='col' id='source'>" + item[1] +
                "</div><div class='col' id='target'>" + item[2] +
                "</div><div class='col' id='description'>" + item[3] +
                "</div></div>"
            ).appendTo('#data_link');
        });
    });
}

get_links_for_term = function (id) {
    $("#form_link").css({ visibility: 'visible' });
    $.getJSON('/get_links_for_term?id=' + id, function (data) {
        $("#one_link").html("");
        $.each(data, function (i, item) {
            $("<div class = 'row'> id = '" + i + '>').html(
                "<div class='col' id='link_id'>" + item[0] +
                "</div><div class='col' id='source'>" + item[1] +
                "</div><div class='col' id='target'>" + item[2] +
                "</div></div>"
            ).appendTo('#one_link');
        });
    });
}

update_data = function (id) {
    $("#form_update").css({ visibility: 'visible' });
    $.getJSON('/get_one_entry?id=' + id, function (data) {
        console.log(data);
        $("input[name~='id']").val(data[0]);
        $("input[name~='value']").val(data[1]);
        $("input[name~='description']").val(data[2]);
    })
}

$(document).mouseup(function (e) {
    var container = $(".form");
    if (!container.is(e.target) && container.has(e.target).length === 0) {
        $(".form").css({ visibility: 'hidden' });
    }
});

$(document).ready(function () {
    fill_data_list();
    fill_links();
    fill_types();
});
