$(document).ready(function () {

    // :::::::::: WORK END DATE :::::::::::

    // //// Ex " 1 "
    $("#id_registration-0-end_date").parent().css("opacity", "0");
    $("#id_registration-0-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-0-until_now").val() == "0") {
        $("#id_registration-0-end_date").parent().css("opacity", "1");
        $("#id_registration-0-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-0-until_now").change(function () {
        var end_date = $("#id_registration-0-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-0-end_date").parent().css("opacity", "0");
                $("#id_registration-0-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-0-end_date").parent().css("opacity", "1");
                $("#id_registration-0-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-0-end_date").parent().css("opacity", "0");
                $("#id_registration-0-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 2 "
    $("#id_registration-1-end_date").parent().css("opacity", "0");
    $("#id_registration-1-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-1-until_now").val() == "0") {
        $("#id_registration-1-end_date").parent().css("opacity", "1");
        $("#id_registration-1-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-1-until_now").change(function () {
        var end_date = $("#id_registration-1-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-1-end_date").parent().css("opacity", "0");
                $("#id_registration-1-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-1-end_date").parent().css("opacity", "1");
                $("#id_registration-1-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-1-end_date").parent().css("opacity", "0");
                $("#id_registration-1-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 3 "
    $("#id_registration-2-end_date").parent().css("opacity", "0");
    $("#id_registration-2-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-2-until_now").val() == "0") {
        $("#id_registration-2-end_date").parent().css("opacity", "1");
        $("#id_registration-2-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-2-until_now").change(function () {
        var end_date = $("#id_registration-2-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-2-end_date").parent().css("opacity", "0");
                $("#id_registration-2-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-2-end_date").parent().css("opacity", "1");
                $("#id_registration-2-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-2-end_date").parent().css("opacity", "0");
                $("#id_registration-2-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 4 "
    $("#id_registration-3-end_date").parent().css("opacity", "0");
    $("#id_registration-3-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-3-until_now").val() == "0") {
        $("#id_registration-3-end_date").parent().css("opacity", "1");
        $("#id_registration-3-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-3-until_now").change(function () {
        var end_date = $("#id_registration-3-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-3-end_date").parent().css("opacity", "0");
                $("#id_registration-3-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-3-end_date").parent().css("opacity", "1");
                $("#id_registration-3-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-3-end_date").parent().css("opacity", "0");
                $("#id_registration-3-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 5 "
    $("#id_registration-4-end_date").parent().css("opacity", "0");
    $("#id_registration-4-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-4-until_now").val() == "0") {
        $("#id_registration-4-end_date").parent().css("opacity", "1");
        $("#id_registration-4-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-4-until_now").change(function () {
        var end_date = $("#id_registration-4-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-4-end_date").parent().css("opacity", "0");
                $("#id_registration-4-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-4-end_date").parent().css("opacity", "1");
                $("#id_registration-4-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-4-end_date").parent().css("opacity", "0");
                $("#id_registration-4-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 6 "
    $("#id_registration-5-end_date").parent().css("opacity", "0");
    $("#id_registration-5-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-5-until_now").val() == "0") {
        $("#id_registration-5-end_date").parent().css("opacity", "1");
        $("#id_registration-5-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-5-until_now").change(function () {
        var end_date = $("#id_registration-5-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-5-end_date").parent().css("opacity", "0");
                $("#id_registration-5-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-5-end_date").parent().css("opacity", "1");
                $("#id_registration-5-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-5-end_date").parent().css("opacity", "0");
                $("#id_registration-5-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 7 "
    $("#id_registration-6-end_date").parent().css("opacity", "0");
    $("#id_registration-6-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-6-until_now").val() == "0") {
        $("#id_registration-6-end_date").parent().css("opacity", "1");
        $("#id_registration-6-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-6-until_now").change(function () {
        var end_date = $("#id_registration-6-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-6-end_date").parent().css("opacity", "0");
                $("#id_registration-6-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-6-end_date").parent().css("opacity", "1");
                $("#id_registration-6-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-6-end_date").parent().css("opacity", "0");
                $("#id_registration-6-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 8 "
    $("#id_registration-7-end_date").parent().css("opacity", "0");
    $("#id_registration-7-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-7-until_now").val() == "0") {
        $("#id_registration-7-end_date").parent().css("opacity", "1");
        $("#id_registration-7-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-7-until_now").change(function () {
        var end_date = $("#id_registration-7-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-7-end_date").parent().css("opacity", "0");
                $("#id_registration-7-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-7-end_date").parent().css("opacity", "1");
                $("#id_registration-7-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-7-end_date").parent().css("opacity", "0");
                $("#id_registration-7-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 9 "
    $("#id_registration-8-end_date").parent().css("opacity", "0");
    $("#id_registration-8-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-8-until_now").val() == "0") {
        $("#id_registration-8-end_date").parent().css("opacity", "1");
        $("#id_registration-8-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-8-until_now").change(function () {
        var end_date = $("#id_registration-8-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-8-end_date").parent().css("opacity", "0");
                $("#id_registration-8-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-8-end_date").parent().css("opacity", "1");
                $("#id_registration-8-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-8-end_date").parent().css("opacity", "0");
                $("#id_registration-8-end_date").next("span > a").attr("disabled");
                break;
        }
    });

    // //// Ex " 10 "
    $("#id_registration-9-end_date").parent().css("opacity", "0");
    $("#id_registration-9-end_date").next("span > a").attr("disabled");

    if ($("#id_registration-9-until_now").val() == "0") {
        $("#id_registration-9-end_date").parent().css("opacity", "1");
        $("#id_registration-9-end_date").next("span > a").removeAttr("disabled");
    }

    $("#id_registration-9-until_now").change(function () {
        var end_date = $("#id_registration-9-until_now").val();
        switch (end_date) {
            case "":
                $("#id_registration-9-end_date").parent().css("opacity", "0");
                $("#id_registration-9-end_date").next("span > a").attr("disabled");
                break;
            case "0":
                $("#id_registration-9-end_date").parent().css("opacity", "1");
                $("#id_registration-9-end_date")
                    .next("span > a")
                    .removeAttr("disabled");
                break;
            case "1":
                $("#id_registration-9-end_date").parent().css("opacity", "0");
                $("#id_registration-9-end_date").next("span > a").attr("disabled");
                break;
        }
    });



    // :::::::::: WORK END DATE :::::::::::

    // //// SAL " 1 "
    $('#id_registration-0-salary').hide();
    if ($("#id_registration-0-if_salary").val() == '1') {
        $('#id_registration-0-salary').show();
    }
    $("#id_registration-0-if_salary").change(function () {
        var sal = $("#id_registration-0-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-0-salary').hide();
                break;
            case "0":
                $('#id_registration-0-salary').hide();
                break;
            case "1":
                $('#id_registration-0-salary').show();
                break;
        }
    });

    // //// SAL " 2 "
    $('#id_registration-1-salary').hide();
    if ($("#id_registration-1-if_salary").val() == '1') {
        $('#id_registration-1-salary').show();
    }
    $("#id_registration-1-if_salary").change(function () {
        var sal = $("#id_registration-1-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-1-salary').hide();
                break;
            case "0":
                $('#id_registration-1-salary').hide();
                break;
            case "1":
                $('#id_registration-1-salary').show();
                break;
        }
    });


    // //// SAL " 3 "
    $('#id_registration-2-salary').hide();
    if ($("#id_registration-2-if_salary").val() == '1') {
        $('#id_registration-2-salary').show();
    }
    $("#id_registration-2-if_salary").change(function () {
        var sal = $("#id_registration-2-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-2-salary').hide();
                break;
            case "0":
                $('#id_registration-2-salary').hide();
                break;
            case "1":
                $('#id_registration-2-salary').show();
                break;
        }
    });

    // //// SAL " 4 "
    $('#id_registration-3-salary').hide();
    if ($("#id_registration-3-if_salary").val() == '1') {
        $('#id_registration-3-salary').show();
    }
    $("#id_registration-3-if_salary").change(function () {
        var sal = $("#id_registration-3-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-3-salary').hide();
                break;
            case "0":
                $('#id_registration-3-salary').hide();
                break;
            case "1":
                $('#id_registration-3-salary').show();
                break;
        }
    });


    // //// SAL " 5 "
    $('#id_registration-4-salary').hide();
    if ($("#id_registration-4-if_salary").val() == '1') {
        $('#id_registration-4-salary').show();
    }
    $("#id_registration-4-if_salary").change(function () {
        var sal = $("#id_registration-4-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-4-salary').hide();
                break;
            case "0":
                $('#id_registration-4-salary').hide();
                break;
            case "1":
                $('#id_registration-4-salary').show();
                break;
        }
    });

    // //// SAL " 6 "
    $('#id_registration-5-salary').hide();
    if ($("#id_registration-5-if_salary").val() == '1') {
        $('#id_registration-5-salary').show();
    }
    $("#id_registration-5-if_salary").change(function () {
        var sal = $("#id_registration-5-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-5-salary').hide();
                break;
            case "0":
                $('#id_registration-5-salary').hide();
                break;
            case "1":
                $('#id_registration-5-salary').show();
                break;
        }
    });

    // //// SAL " 7 "
    $('#id_registration-6-salary').hide();
    if ($("#id_registration-6-if_salary").val() == '1') {
        $('#id_registration-6-salary').show();
    }
    $("#id_registration-6-if_salary").change(function () {
        var sal = $("#id_registration-6-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-6-salary').hide();
                break;
            case "0":
                $('#id_registration-6-salary').hide();
                break;
            case "1":
                $('#id_registration-6-salary').show();
                break;
        }
    });

    // //// SAL " 8 "
    $('#id_registration-7-salary').hide();
    if ($("#id_registration-7-if_salary").val() == '1') {
        $('#id_registration-7-salary').show();
    }
    $("#id_registration-7-if_salary").change(function () {
        var sal = $("#id_registration-7-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-7-salary').hide();
                break;
            case "0":
                $('#id_registration-7-salary').hide();
                break;
            case "1":
                $('#id_registration-7-salary').show();
                break;
        }
    });


    // //// SAL " 9 "
    $('#id_registration-8-salary').hide();
    if ($("#id_registration-8-if_salary").val() == '1') {
        $('#id_registration-8-salary').show();
    }
    $("#id_registration-8-if_salary").change(function () {
        var sal = $("#id_registration-8-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-8-salary').hide();
                break;
            case "0":
                $('#id_registration-8-salary').hide();
                break;
            case "1":
                $('#id_registration-8-salary').show();
                break;
        }
    });


    // //// SAL " 10 "
    $('#id_registration-9-salary').hide();
    if ($("#id_registration-9-if_salary").val() == '1') {
        $('#id_registration-9-salary').show();
    }
    $("#id_registration-9-if_salary").change(function () {
        var sal = $("#id_registration-9-if_salary").val();
        switch (sal) {
            case "":
                $('#id_registration-9-salary').hide();
                break;
            case "0":
                $('#id_registration-9-salary').hide();
                break;
            case "1":
                $('#id_registration-9-salary').show();
                break;
        }
    });



});