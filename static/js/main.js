$(document).ready(function () {
    $('#div_id_image').addClass('row d-block');
    $('#id_birth_date').attr('type', 'date');
    $('#id_date_stop_work').attr('type', 'date');


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
            case '1':
                $('div#div_id_details').hide();
                break;
            case '0':
                $('div#div_id_details').show();
                break;

            default:
                break;
        }
    });


    // Experience
    $('#add_more').click(function () {
        var form_idx = $('#id_form-TOTAL_FORMS').val();
        $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });

});