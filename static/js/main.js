$(document).ready(function () {
    $('#div_id_image').addClass('row d-block');
    $('#id_birth_date').attr('type', 'date');
    $('#id_date_stop_work').attr('type', 'date');


    // ALERT 
    $(".alert").delay(6000).slideUp(1000, function () {
        $(this).alert('close');
    });

    // :::::::::::::: PROFILE :::::::::::::::

    $('#div_id_region').hide();
    if ($('#id_country').val() == "SY") {
        $('#div_id_region').show();
    }
    $('#id_country').change(function () {
        var medical = $('#id_country').val();
        switch (medical) {
            case 'SY':
                $('div#div_id_region').show();
                break;
            case '':
                $('div#div_id_region').hide();
                break;
            default:
                $('div#div_id_region').hide();
                break;
        }
    });

    $('#div_id_current_region').hide();
    if ($('#id_current_country').val() == 'SY') {
        $('#div_id_current_region').show();
    }
    $('#id_current_country').change(function () {
        var medical = $('#id_current_country').val();
        switch (medical) {
            case 'SY':
                $('div#div_id_current_region').show();
                break;
            case '':
                $('div#div_id_current_region').hide();
                break;
            default:
                $('div#div_id_current_region').hide();
                break;
        }
    });


    // :::::::: MEDICAL INFO :::::::::::: 
    $('div#div_id_medical_state_des').hide();
    $('#id_medical_state_q').change(function () {
        var medical = $('#id_medical_state_q').val();
        switch (medical) {
            case '':
                $('div#div_id_medical_state_des').hide();
                break;
            case '0':
                $('div#div_id_medical_state_des').hide();
                break;
            case '1':
                $('div#div_id_medical_state_des').show();
                break;

        }
    });

    /////////////////////// Family status Hide/Show
    $(
        "div#div_id_have_kids,div#div_id_number_kids,div#div_id_summary_of_recsituation"
    ).hide();

    if (
        $("#id_family_state").val() == "married" ||
        $("#id_family_state").val() == "widow" ||
        $("#id_family_state").val() == "divorced"
    ) {
        $("div#div_id_have_kids").show();
        $("div#div_id_summary_of_recsituation").show();
    }

    $("#id_family_state").change(function () {
        var family_state = $("#id_family_state").val();
        switch (family_state) {
            case "":
                $("div#div_id_summary_of_recsituation").hide();
                $("div#div_id_have_kids").hide();
                $("div#div_id_number_kids").hide();
                break;
            case "single":
                $("div#div_id_summary_of_recsituation").hide();
                $("div#div_id_have_kids").hide();
                $("div#div_id_number_kids").hide();
                break;
            case "married":
                $("div#div_id_summary_of_recsituation").show();
                $("div#div_id_have_kids").show();
                break;
            case "widow":
                $("div#div_id_summary_of_recsituation").show();
                $("div#div_id_have_kids").show();
                break;
            case "divorced":
                $("div#div_id_summary_of_recsituation").show();
                $("div#div_id_have_kids").show();
                break;
        }
    });

    if ($("#id_have_kids").val() == "1") {
        $("div#div_id_number_kids").show();
    }

    $("#id_have_kids").change(function () {
        var have_kids = $("#id_have_kids").val();
        switch (have_kids) {
            case "":
                $("div#div_id_number_kids").hide();
                break;
            case "0":
                $("div#div_id_number_kids").hide();
                break;
            case "1":
                $("div#div_id_number_kids").show();
                break;
        }
    });
    // ///////////// END FAMILY SATE /////////////


    // ::::::::::::::: WORK ::::::::::::::
    $('div#div_id_details').hide();
    $('#id_org_memeber').change(function () {
        var org = $('#id_org_memeber').val();
        switch (org) {
            case '':
                $('div#div_id_details').hide();
                break;
            case '0':
                $('div#div_id_details').hide();
                break;
            case '1':
                $('div#div_id_details').show();
                break;

            default:
                break;
        }
    });


    // ::::::::::::: EXPERIENCES :::::::::::::::
    $('div.form-exper').hide();
    if ($('#id_experience').val() == '1') {
        $('div.form-exper').show();
    }
    $('#id_experience').change(function () {
        var org = $('#id_experience').val();
        switch (org) {
            case '':
                $('div.form-exper').hide();
                break;
            case '0':
                $('div.form-exper').hide();
                break;
            case '1':
                $('div.form-exper').show();
                break;
        }
    });


    // Experience BTN
    var form_idx = 0
    $('#add_more_ex').click(function () {
        form_idx++;
        // var form_idx = $('#id_form-TOTAL_FORMS').val();
        $('#form_set_ex').append($('#empty_form_ex').html().replace(/__prefix__/g, form_idx));
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);


        // End-Date field 
        $('#id_form-' + form_idx + '-start_date').attr('type', 'date');
        $('#id_form-' + form_idx + '-end_date').attr('type', 'date')
        $('#div_id_form-' + form_idx + '-end_date').hide();
        if ($('#id_form-' + form_idx + '-until_now').val() == "0") {
            $('#div_id_form-' + form_idx + '-end_date').show();
        }
        $('#id_form-' + form_idx + '-until_now').change(function () {
            var org = $('#id_form-' + form_idx + '-until_now').val();
            switch (org) {
                case '':
                    $('#div_id_form-' + form_idx + '-end_date').hide();
                    break;
                case '1':
                    $('#div_id_form-' + form_idx + '-end_date').hide();
                    break;
                case '0':
                    $('#div_id_form-' + form_idx + '-end_date').show();
                    break;
            }
        });


        // Salary 
        $('#div_id_form-' + form_idx + '-salary').hide();
        if ($('#id_form-' + form_idx + '-if_salary').val() == '1') {
            $('#div_id_form-' + form_idx + '-salary').show();
        }
        $('#id_form-' + form_idx + '-if_salary').change(function () {
            var org = $('#id_form-' + form_idx + '-if_salary').val();
            switch (org) {
                case '':
                    $('#div_id_form-' + form_idx + '-salary').hide();
                    break;
                case '0':
                    $('#div_id_form-' + form_idx + '-salary').hide();
                    break;
                case '1':
                    $('#div_id_form-' + form_idx + '-salary').show();
                    break;
            }
        });





    });




    // :::::::::::::::::: VIOLATIONS :::::::::::::::::::
    $('div.form-vio').hide();
    if ($('#id_violations').val() == '1') {
        $('div.form-vio').show();
    }
    $('#id_violations').change(function () {
        var org = $('#id_violations').val();
        switch (org) {
            case '':
                $('div.form-vio').hide();
                break;
            case '0':
                $('div.form-vio').hide();
                break;
            case '1':
                $('div.form-vio').show();
                break;
        }
    });


    // Violations BTN
    var form_idx = 0
    $('#add_more_vio').click(function () {
        form_idx++;
        // var form_idx = $('#id_form-TOTAL_FORMS').val();
        $('#form_set_vio').append($('#empty_form_vio').html().replace(/__prefix__/g, form_idx));
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);

        // Date vio
        $('#id_form-' + form_idx + '-date_of_violation').attr('type', 'date');

    });

    // Relations
    $('#div_id_summary_of_relations').hide();
    if ($('#id_relation_with_org').val() == "1") {
        $('#div_id_summary_of_relations').hide();
    }
    $('#id_relation_with_org').change(function () {
        var org = $('#id_relation_with_org').val();
        switch (org) {
            case '':
                $('#div_id_summary_of_relations').hide();
                break;
            case '0':
                $('#div_id_summary_of_relations').hide();
                break;
            case '1':
                $('#div_id_summary_of_relations').show();
                break;
        }
    });



    // Summary Générale
    $('#div_id_articls_link_1').hide();
    if ($('#id_if_article_linke').val == '1') {
        $('#div_id_articls_link_1').show();
    }
    $('#id_if_article_linke').change(function () {
        var org = $('#id_if_article_linke').val();
        switch (org) {
            case '':
                $('#div_id_articls_link_1').hide();
                break;
            case '0':
                $('#div_id_articls_link_1').hide();
                break;
            case '1':
                $('#div_id_articls_link_1').show();
                break;
        }
    });

    // Stop Work in Média
    $('#div_id_date_stop_work').hide();
    if ($('#id_if_stop_work').val == "1") {
        $('#div_id_date_stop_work').show();
    }
    $('#id_if_stop_work').change(function () {
        var org = $('#id_if_stop_work').val();
        switch (org) {
            case '':
                $('#div_id_date_stop_work').hide();
                break;
            case '0':
                $('#div_id_date_stop_work').hide();
                break;
            case '1':
                $('#div_id_date_stop_work').show();
                break;
        }
    });

    // Resource 
    var res_group = $('#div_id_recmond_1, #div_id_phon_1, #div_id_email_1, #div_id_recmond_2, #div_id_phon_2, #div_id_email_2');
    res_group.hide();
    if ($('#id_resource_prof').val() == "1") {
        res_group.show();
    }
    $('#id_resource_prof').change(function () {
        var org = $('#id_resource_prof').val();
        switch (org) {
            case '':
                res_group.hide();
                break;
            case '0':
                res_group.hide();
                break;
            case '1':
                res_group.show();
                break;
        }
    });



    // parteciper
    $('#div_id_details_traning_media').hide();
    if ($('#id_training_media').val() == "1") {
        $('#div_id_details_traning_media').hide();
    }
    $('#id_training_media').change(function () {
        var org = $('#id_training_media').val();
        switch (org) {
            case '':
                $('#div_id_details_traning_media').hide();
                break;
            case '0':
                $('#div_id_details_traning_media').hide();
                break;
            case '1':
                $('#div_id_details_traning_media').show();
                break;
        }
    });


    $('#id_date_of_demand_org').attr('type', 'date');

    var ques_group = $('#div_id_name_org, #div_id_date_of_demand_org, #div_id_type_of_demand_other_org, #div_id_result_of_demand_other_org');
    ques_group.hide();
    if ($('#id_other_org_demand').val() == "1") {
        ques_group.show();
    }
    $('#id_other_org_demand').change(function () {
        var org = $('#id_other_org_demand').val();
        switch (org) {
            case '':
                ques_group.hide();
                break;
            case '0':
                ques_group.hide();
                break;
            case '1':
                ques_group.show();
                break;
        }
    });


    // Support tools
    $('#div_id_list_of_tools').hide();
    if ($('#id_type_of_dmande').val() == "8") {
        $('#div_id_list_of_tools').hide();
    }
    $('#id_type_of_dmande').change(function () {
        var org = $('#id_type_of_dmande').val();
        switch (org) {
            case '':
                $('#div_id_list_of_tools').hide();
                break;
            case '8':
                $('#div_id_list_of_tools').show();
                break;
            default:
                $('#div_id_list_of_tools').hide();
                break;
        }
    });







});