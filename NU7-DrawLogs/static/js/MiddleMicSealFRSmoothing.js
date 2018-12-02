var title = "Middle_Mic_Seal_FR_Smoothing";
var jsonDataDir = "../jsonData/Middle_Mic_Seal_FR_Smoothing.json";

$.getJSON(jsonDataDir, function (data) {
    var idStr = "showAllBox";
    showAll(data, idStr, title, mictablefunc, micXdata);
});

function showSingleBtn() {
    $("#showAllBox").css('display', 'none');
    $("#showSingleBox").css('display', 'block');
    $("#seldialog").css('display', 'none');
    $("#showSearchBox").css('display', 'none');
    var idStr = "showSingleBox";
    $.getJSON(jsonDataDir, function (data) {
        showSingle(data, idStr, title, micXdata)
    })
};

function selectBtn() {
    $("#showAllBox").css('display', 'none');
    $("#showSingleBox").css('display', 'none');
    $("#seldialog").css('display', 'none');
    $("#showSearchBox").css('display', 'block');
    $.getJSON(jsonDataDir, function (data) {
        handlerData = filterData(data, "select")
        var idStr = "showSearchBox";
        showAll(handlerData, idStr, title, mictablefunc,micXdata )
    })
    
};

function ignoreBtn() {
    $("#showAllBox").css('display', 'none');
    $("#showSingleBox").css('display', 'none');
    $("#seldialog").css('display', 'none');
    $("#showSearchBox").css('display', 'block');
    $.getJSON(jsonDataDir, function (data) {
        handlerData = filterData(data, "ignore")
        var idStr = "showSearchBox";
        showAll(handlerData, idStr, title, mictablefunc,micXdata)
    })
};

