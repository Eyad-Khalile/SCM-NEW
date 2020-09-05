$(document).ready(function () {

    // :::::::::: WORK END DATE :::::::::::

    // alert('Salut');


    $('tr.add-row td').find('a').click(function () {

        // //// Ex " 1 "
        $("#id_registration_media_act-0-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-0-until_now").val() == '0') {
            $("#id_registration_media_act-0-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-0-until_now').change(function () {
            var org = $('#id_registration_media_act-0-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-0-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-0-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-0-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });

        // //// Ex " 2 "
        $("#id_registration_media_act-1-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-1-until_now").val() == '0') {
            $("#id_registration_media_act-1-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-1-until_now').change(function () {
            var org = $('#id_registration_media_act-1-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-1-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-1-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-1-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });


        // //// Ex " 3 "
        $("#id_registration_media_act-2-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-2-until_now").val() == '0') {
            $("#id_registration_media_act-2-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-2-until_now').change(function () {
            var org = $('#id_registration_media_act-2-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-2-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-2-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-2-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });


        // //// Ex " 4 "
        $("#id_registration_media_act-3-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-3-until_now").val() == '0') {
            $("#id_registration_media_act-3-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-3-until_now').change(function () {
            var org = $('#id_registration_media_act-3-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-3-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-3-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-3-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });


        // //// Ex " 5 "
        $("#id_registration_media_act-4-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-4-until_now").val() == '0') {
            $("#id_registration_media_act-4-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-4-until_now').change(function () {
            var org = $('#id_registration_media_act-4-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-4-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-4-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-4-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });

        // //// Ex " 6 "
        $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-5-until_now").val() == '0') {
            $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-5-until_now').change(function () {
            var org = $('#id_registration_media_act-5-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });


        // //// Ex " 6 "
        $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-5-until_now").val() == '0') {
            $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-5-until_now').change(function () {
            var org = $('#id_registration_media_act-5-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-5-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });


        // //// Ex " 7 "
        $("#id_registration_media_act-6-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-6-until_now").val() == '0') {
            $("#id_registration_media_act-6-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-6-until_now').change(function () {
            var org = $('#id_registration_media_act-6-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-6-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-6-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-6-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });


        // //// Ex " 8 "
        $("#id_registration_media_act-7-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-7-until_now").val() == '0') {
            $("#id_registration_media_act-7-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-7-until_now').change(function () {
            var org = $('#id_registration_media_act-7-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-7-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-7-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-7-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });


        // //// Ex " 9 "
        $("#id_registration_media_act-8-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-8-until_now").val() == '0') {
            $("#id_registration_media_act-8-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-8-until_now').change(function () {
            var org = $('#id_registration_media_act-8-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-8-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-8-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-8-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });


        // //// Ex " 10 "
        $("#id_registration_media_act-9-end_date").parent('td.field-end_date').css("opacity", "0");
        if ($("#id_registration_media_act-9-until_now").val() == '0') {
            $("#id_registration_media_act-9-end_date").parent('td.field-end_date').css("opacity", "1");
        }
        $('#id_registration_media_act-9-until_now').change(function () {
            var org = $('#id_registration_media_act-9-until_now').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-9-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-9-end_date").parent('td.field-end_date').css("opacity", "1");
                    break;
                case '1':
                    $("#id_registration_media_act-9-end_date").parent('td.field-end_date').css("opacity", "0");
                    break;
            }
        });

        // :::::::::::::::::::: SALARY :::::::::::::::::::
        // //// Ex " 1 "
        $("#id_registration_media_act-0-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-0-if_salary").val() == '1') {
            $("#id_registration_media_act-0-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-0-if_salary').change(function () {
            var org = $('#id_registration_media_act-0-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-0-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-0-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-0-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 2 "
        $("#id_registration_media_act-1-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-1-if_salary").val() == '1') {
            $("#id_registration_media_act-1-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-1-if_salary').change(function () {
            var org = $('#id_registration_media_act-1-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-1-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-1-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-1-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 3 "
        $("#id_registration_media_act-2-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-2-if_salary").val() == '1') {
            $("#id_registration_media_act-2-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-2-if_salary').change(function () {
            var org = $('#id_registration_media_act-2-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-2-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-2-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-2-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 4 "
        $("#id_registration_media_act-3-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-3-if_salary").val() == '1') {
            $("#id_registration_media_act-3-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-3-if_salary').change(function () {
            var org = $('#id_registration_media_act-3-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-3-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-3-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-3-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 5 "
        $("#id_registration_media_act-4-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-4-if_salary").val() == '1') {
            $("#id_registration_media_act-4-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-4-if_salary').change(function () {
            var org = $('#id_registration_media_act-4-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-4-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-4-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-4-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 6 "
        $("#id_registration_media_act-5-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-5-if_salary").val() == '1') {
            $("#id_registration_media_act-5-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-5-if_salary').change(function () {
            var org = $('#id_registration_media_act-5-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-5-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-5-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-5-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 7 "
        $("#id_registration_media_act-6-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-6-if_salary").val() == '1') {
            $("#id_registration_media_act-6-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-6-if_salary').change(function () {
            var org = $('#id_registration_media_act-6-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-6-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-6-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-6-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 8 "
        $("#id_registration_media_act-7-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-7-if_salary").val() == '1') {
            $("#id_registration_media_act-7-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-7-if_salary').change(function () {
            var org = $('#id_registration_media_act-7-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-7-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-7-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-7-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 9 "
        $("#id_registration_media_act-8-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-8-if_salary").val() == '1') {
            $("#id_registration_media_act-8-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-8-if_salary').change(function () {
            var org = $('#id_registration_media_act-8-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-8-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-8-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-8-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });

        // //// Ex " 10 "
        $("#id_registration_media_act-9-salary").parent('td.field-salary').css("opacity", "0");
        if ($("#id_registration_media_act-9-if_salary").val() == '1') {
            $("#id_registration_media_act-9-salary").parent('td.field-salary').css("opacity", "1");
        }
        $('#id_registration_media_act-9-if_salary').change(function () {
            var org = $('#id_registration_media_act-9-if_salary').val();
            switch (org) {
                case '':
                    $("#id_registration_media_act-9-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '0':
                    $("#id_registration_media_act-9-salary").parent('td.field-salary').css("opacity", "0");
                    break;
                case '1':
                    $("#id_registration_media_act-9-salary").parent('td.field-salary').css("opacity", "1");
                    break;
            }
        });



    });





});
django.jQuery;