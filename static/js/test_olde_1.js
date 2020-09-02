if (!$) {
    // Need this line because Django also provided jQuery and namespaced as django.jQuery
    $ = django.jQuery;
}
//////////////////////////////////////////////function to replace the urls  into links
$(document).ready(function () {
    function linkify(inputText) {
        var replacedText, replacePattern1, replacePattern2, replacePattern3;

        //URLs starting with http://, https://, or ftp://
        replacePattern1 = /(\b(https?|ftp):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/gim;
        replacedText = inputText.replace(
            replacePattern1,
            '<a href="$1" target="_blank">$1</a>'
        );

        //URLs starting with "www." (without // before it, or it'd re-link the ones done above).
        replacePattern2 = /(^|[^\/])(www\.[\S]+(\b|$))/gim;
        replacedText = replacedText.replace(
            replacePattern2,
            '$1<a href="http://$2" target="_blank">$2</a>'
        );

        //Change email addresses to mailto:: links.
        replacePattern3 = /(([a-zA-Z0-9\-\_\.])+@[a-zA-Z\_]+?(\.[a-zA-Z]{2,6})+)/gim;
        replacedText = replacedText.replace(
            replacePattern3,
            '<a href="mailto:$1">$1</a>'
        );

        return replacedText;
    }
    var text = $("#id_articls_link_1").val();
});
// function to states processing 
$(document).ready(function () {
    $(function () {
        $('.first_step').hide();
        $('.second_step').hide();
        $('.third_step').hide();
        $('.forth_step').hide();
        $('.upload_files').hide();


        // $('.abcdefgh').hide();
        $('#id_state_step').change(function () {
            $('.upload_files').hide();
            // $('.abcdefgh').hide();
            if (this.options[this.selectedIndex].value == '2') {
                $('.first_step').show();

            }
            if (this.options[this.selectedIndex].value == '3') {
                $('.second_step').show();
            }
            if (this.options[this.selectedIndex].value == '4') {
                $('.third_step').show();
            }
            if (this.options[this.selectedIndex].value == '5') {
                $('.forth_step').show();
            }
            if (this.options[this.selectedIndex].value == '5') {
                $('.upload_files').show();
            }

        });

    });
});
//function to hide yes and no qustions from regestration admin interface
/////////////////////////////////////////////////////////////////////////
$(document).ready(function () {
    $(function () {
        // Medical status
        $("label[for=id_medical_note_inf],#id_medical_note_inf").hide();
        if ($("#id_medical_state_inf").val() == "0") {
            $("label[for=id_medical_note_inf],#id_medical_note_inf").show();
        }

        $("#id_medical_state_inf").change(function () {
            var medical = $("#id_medical_state_inf").val();
            switch (medical) {
                case "0":
                    $("label[for=id_medical_note_inf],#id_medical_note_inf").show();
                    break;
                case "1":
                    $("label[for=id_medical_note_inf],#id_medical_note_inf").hide();
                    break;
                case "":
                    $("label[for=id_medical_note_inf],#id_medical_note_inf").hide();
                    break;
                    // default:
                    //   $('label[for=id_medical_note_inf],#id_medical_note_inf').hide();
            }
        });




        // ::::::::::::::::::::: MEDICAL STATUS :::::::::::::::::
        $('div.fieldBox.field-medical_state_des').hide();
        if ($('#id_medical_state_q').val() == '1') {
            $('div.fieldBox.field-medical_state_des').show();
        }

        $("#id_medical_state_q").change(function () {
            var medical = $("#id_medical_state_q").val();
            switch (medical) {
                case "":
                    $('div.fieldBox.field-medical_state_des').hide();
                    break;
                case "0":
                    $('div.fieldBox.field-medical_state_des').hide();
                    break;
                case "1":
                    $('div.fieldBox.field-medical_state_des').show();
                    break;
            }
        });


        ////////////////////// Phone status
        $("label[for=id_phone],#id_phone").hide();
        if ($("#id_phone_state_inf").val() == "1") {
            $("label[for=id_phone],#id_phone").show();
        }
        $("#id_phone_state_inf").change(function () {
            var phone = $("#id_phone_state_inf").val();
            switch (phone) {
                case "":
                    $("label[for=id_phone],#id_phone").hide();
                    break;
                case "0":
                    $("label[for=id_phone],#id_phone").hide();
                    break;
                case "1":
                    $("label[for=id_phone],#id_phone").show();
                    break;
            }
        });

        /////////////////// Facebook status
        $("label[for=id_facebook],#id_facebook").hide();
        if ($("#id_facebook_state_inf").val() == "1") {
            $("label[for=id_facebook],#id_facebook").show();
        }
        $("#id_facebook_state_inf").change(function () {
            var phone = $("#id_facebook_state_inf").val();
            switch (phone) {
                case "":
                    $("label[for=id_facebook],#id_facebook").hide();
                    break;
                case "0":
                    $("label[for=id_facebook],#id_facebook").hide();
                    break;
                case "1":
                    $("label[for=id_facebook],#id_facebook").show();
                    break;
            }
        });

        /////////////////////// Family status Hide/Show
        $(
            "div.field-have_kids,div.field-number_kids,div.field-summary_of_recsituation"
        ).hide();

        if (
            $("#id_family_state").val() == "married" ||
            $("#id_family_state").val() == "widow" ||
            $("#id_family_state").val() == "divorced"
        ) {
            $("div.field-have_kids").show();
            $("div.field-summary_of_recsituation").show();
        }

        $("#id_family_state").change(function () {
            var family_state = $("#id_family_state").val();
            switch (family_state) {
                case "":
                    $("div.field-summary_of_recsituation").hide();
                    $("div.field-have_kids").hide();
                    $("div.field-number_kids").hide();
                    break;
                case "single":
                    $("div.field-summary_of_recsituation").hide();
                    $("div.field-have_kids").hide();
                    $("div.field-number_kids").hide();
                    break;
                case "married":
                    $("div.field-summary_of_recsituation").show();
                    $("div.field-have_kids").show();
                    break;
                case "widow":
                    $("div.field-summary_of_recsituation").show();
                    $("div.field-have_kids").show();
                    break;
                case "divorced":
                    $("div.field-summary_of_recsituation").show();
                    $("div.field-have_kids").show();
                    break;
            }
        });

        if ($("#id_have_kids").val() == "1") {
            $("div.field-number_kids").show();
        }

        $("#id_have_kids").change(function () {
            var have_kids = $("#id_have_kids").val();
            switch (have_kids) {
                case "":
                    $("div.field-number_kids").hide();
                    break;
                case "0":
                    $("div.field-number_kids").hide();
                    break;
                case "1":
                    $("div.field-number_kids").show();
                    break;
            }
        });
        // ///////////// END FAMILY SATE /////////////

        // ::::::::::::::: LINKE OF WORK ::::::::::::::::::::

        $("div.fieldBox.field-articls_link_1").hide();
        if ($("#id_if_article_linke").val() == "1") {
            $("div.fieldBox.field-articls_link_1").show();
        } else if ($("#id_if_article_linke").val() == "") {
            $("div.fieldBox.field-articls_link_1").hide();
        }

        $("#id_if_article_linke").change(function () {
            var pub = $("#id_if_article_linke").val();

            switch (pub) {
                case "":
                    $("div.fieldBox.field-articls_link_1").hide();
                    break;
                case "0":
                    $("div.fieldBox.field-articls_link_1").hide();
                    break;
                case "1":
                    $("div.fieldBox.field-articls_link_1").show();
                    break;
            }
        });

        $("div.fieldBox.field-date_stop_work").hide();
        if ($("#id_if_stop_work").val() == "1") {
            $("div.fieldBox.field-date_stop_work").show();
        }

        $("#id_if_stop_work").change(function () {
            var date = $("#id_if_stop_work").val();

            switch (date) {
                case "":
                    $("div.fieldBox.field-date_stop_work").hide();
                    break;
                case "0":
                    $("div.fieldBox.field-date_stop_work").hide();
                    break;
                case "1":
                    $("div.fieldBox.field-date_stop_work").show();
                    break;
            }
        });

        $("div.form-row.field-experience").find("fieldset").hide();
        if ($("#id_experience").val() == "1") {
            $("div.form-row.field-experience").find("fieldset").show();
        }

        $("#id_experience").change(function () {
            var exp = $("#id_experience").val();
            switch (exp) {
                case "":
                    $("div.form-row.field-experience").find("fieldset").hide();
                    break;
                case "0":
                    $("div.form-row.field-experience").find("fieldset").hide();
                    break;
                case "1":
                    $("div.form-row.field-experience").find("fieldset").show();
                    break;
            }
        });

        // ::::::::::: PROF EXPERIENCE ::::::::::::::::
        // $("div.form-row.field-recmond_1, div.form-row.field-recmond_2").hide();
        // if ($("#id_resource_prof").val() == "1") {
        //     $("div.form-row.field-recmond_1, div.form-row.field-recmond_2").show();
        // }

        // $("#id_resource_prof").change(function () {
        //     var exp = $("#id_resource_prof").val();
        //     switch (exp) {
        //         case "":
        //             $(
        //                 "div.form-row.field-recmond_1, div.form-row.field-recmond_2"
        //             ).hide();
        //             break;
        //         case "0":
        //             $(
        //                 "div.form-row.field-recmond_1, div.form-row.field-recmond_2"
        //             ).hide();
        //             break;
        //         case "1":
        //             $(
        //                 "div.form-row.field-recmond_1, div.form-row.field-recmond_2"
        //             ).show();
        //             break;
        //     }
        // });

        // :::::::::::::::::: الانتهاكات :::::::::::::::::::
        $("div#violation_set-group").hide();
        if ($("#id_violations").val() == "1") {
            $("div#violation_set-group").show();
        }

        $("#id_violations").change(function () {
            var vio = $("#id_violations").val();
            switch (vio) {
                case "":
                    $("div#violation_set-group").hide();
                    break;
                case "0":
                    $("div#violation_set-group").hide();
                    break;
                case "1":
                    $("div#violation_set-group").show();
                    break;
            }
        });

        // :::::::::::::::::::: RELATIONS ::::::::::::::::::::::

        $("div.fieldBox.field-summary_of_relations").hide();
        if ($("#id_relation_with_org").val() == "1") {
            $("div.fieldBox.field-summary_of_relations").show();
        }
        $("#id_relation_with_org").change(function () {
            var rel = $("#id_relation_with_org").val();
            switch (rel) {
                case "":
                    $("div.fieldBox.field-summary_of_relations").hide();
                    break;
                case "0":
                    $("div.fieldBox.field-summary_of_relations").hide();
                    break;
                case "1":
                    $("div.fieldBox.field-summary_of_relations").show();
                    break;
            }
        });

        // ::::::::::::: OTHER INFORMATIONS :::::::::::::

        // $(
        //     "div.form-row.field-name_org, div.form-row.field-tyoe_of_demand_other_org"
        // ).hide();
        $('div.form-row.field-name_org.field-date_of_demand_org, div.form-row.field-result_of_demand_other_org').hide();

        if ($("#id_other_org_demand").val() == "1") {
            $(
                'div.form-row.field-name_org.field-date_of_demand_org, div.form-row.field-result_of_demand_other_org'
            ).show();
        }

        $("#id_other_org_demand").change(function () {
            var demande = $("#id_other_org_demand").val();
            switch (demande) {
                case "":
                    $(
                        "div.form-row.field-name_org.field-date_of_demand_org, div.form-row.field-result_of_demand_other_org"
                    ).hide();
                    break;
                case "0":
                    $(
                        "div.form-row.field-name_org.field-date_of_demand_org, div.form-row.field-result_of_demand_other_org"
                    ).hide();
                    break;
                case "1":
                    $(
                        "div.form-row.field-name_org.field-date_of_demand_org, div.form-row.field-result_of_demand_other_org"
                    ).show();
                    break;
            }
        });


        // SUPPORT TECHNIQUE
        $('div.form-row.field-list_of_tools').hide();
        if ($('#id_type_of_dmande').val() == '8') {
            $('div.form-row.field-list_of_tools').show();
        }

        $("#id_type_of_dmande").change(function () {
            var demande = $("#id_type_of_dmande").val();
            switch (demande) {
                case "":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "0":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "1":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "2":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "3":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "4":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "5":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "6":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "7":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "8":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).show();
                    break;
                case "9":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "10":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "11":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
                case "12":
                    $(
                        'div.form-row.field-list_of_tools'
                    ).hide();
                    break;
            }
        });




        // $('label[for=id_have_kids],#id_have_kids,.field-have_kids,.field-number_kids,.field-summary_of_recsituation').hide();
        // if ($('#id_family_state').val() == 'متزوج') {
        //   $('label[for=id_have_kids],#id_have_kids.field-have_kids,.field-number_kids,.field-summary_of_recsituation').show();
        // }
        // $('#id_family_state').change(function () {
        //   var paid = $('#id_family_state').val()
        //   switch (paid) {
        //     case 'متزوج':
        //       $('label[for=id_have_kids],#id_have_kids.field-have_kids,.field-number_kids,.field-summary_of_recsituation').show();
        //       break;
        //     case 'عازب':
        //       $('label[for=id_have_kids],#id_have_kids.field-have_kids,.field-number_kids,.field-summary_of_recsituation').hide();
        //       break;
        //   }

        // });

        // if ($('#id_have_kids').val() == '1') {
        //   $('label[for=id_number_kids],#id_number_kids').hide();
        //   $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').hide();

        // }
        // $('#id_have_kids').change(function () {
        //   var kids = $('#id_have_kids').val()
        //   switch (kids) {
        //     case '0':
        //       $('label[for=id_number_kids],#id_number_kids').show();
        //       $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').show();

        //       break;
        //     case '1':
        //       $('label[for=id_number_kids],#id_number_kids').hide();
        //       $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').hide();

        //       break;
        //     default:
        //       $('label[for=id_number_kids],#id_number_kids').hide();
        //       $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').hide();

        //   }

        // });

        // if ($('#id_relation_with_org').val() == '1') {
        //   $('label[for=id_number_kids],#id_number_kids').hide();
        //   $('label[for=id_summary_of_recsituation],#id_summary_of_recsituation').hide();

        // }
        // $('#id_relation_with_org').change(function () {
        //   var kids = $('#id_relation_with_org').val()
        //   switch (kids) {
        //     case '0':
        //       $('label[for=id_summary_of_relations],#id_summary_of_relations').show();

        //       break;
        //     case '1':
        //       $('label[for=id_summary_of_relations],#id_summary_of_relations').hide();
        //       break;
        //     default:
        //       $('label[for=id_summary_of_relations],#id_summary_of_relations').hide();

        //   }

        // });

        // //////////// WORK DETAILS
        // $('th.column-end_date, th.column-salary, td.field-end_date, td.field-salary').hide();

        // if ($('td.field-until_now').find('select').val() == '0') {
        //   $('th.column-end_date, td.field-end_date').show();
        // }

        // $('td.field-until_now').find('select').change(function () {
        //   var date = $(this).val();
        //   switch (date) {
        //     case '0':
        //       $('th.column-end_date, td.field-end_date').show();
        //       break;
        //     case '1':
        //       $('th.column-end_date, td.field-end_date').hide();
        //       break;
        //   }

        // });

        // $("select[name$='until_now']").change(function () {

        //   var date = ("select[name$='until_now']").val();
        //   switch (date) {
        //     case '0':
        //       $('th.column-end_date, td.field-end_date').show();
        //       break;
        //     case '1':
        //       $('th.column-end_date, td.field-end_date').hide();
        //       break;
        //   }

        // });

        // for (i = 0; i < 11; i++) {
        //   $('#id_registration-'+i+'-until_now').change(function () {
        //     var date = $('#id_registration-'+i+'-until_now').val();
        //     console.log(date);
        //     switch (date) {
        //       case '0':
        //         $('th.column-end_date, td.field-end_date').show();
        //         break;
        //       case '1':
        //         $('th.column-end_date, td.field-end_date').hide();
        //         break;
        //     }
        //   });

        // }
    });
});
///////////////////////////////////////////////////////
//function to show and hide violation block

////////////////////////////////////////:
//function to hide and show the media traning block
$(document).ready(function () {
    $(function () {
        $("label[for=id_details_traning_media],#id_details_traning_media").hide();
        if ($("#id_training_media").val() == "1") {
            $("label[for=id_details_traning_media],#id_details_traning_media").show();
        }

        $("#id_training_media").change(function () {
            var medical = $("#id_training_media").val();
            switch (medical) {
                case "":
                    $(
                        "label[for=id_details_traning_media],#id_details_traning_media"
                    ).hide();
                    break;
                case "1":
                    $(
                        "label[for=id_details_traning_media],#id_details_traning_media"
                    ).show();
                    break;
                case "0":
                    $(
                        "label[for=id_details_traning_media],#id_details_traning_media"
                    ).hide();
                    break;
                    // default:
                    //     $(
                    //         "label[for=id_details_traning_media],#id_details_traning_media"
                    //     ).hide();
            }
        });
    });
});
//************************************************************ */
$(document).ready(function () {
    $(function () {
        if ($("#id_paid_job").val() == "1") {
            $("label[for=id_name_of_company_paid],#id_name_of_company_paid").hide();
        }
        $("#id_paid_job").change(function () {
            var paid = $("#id_paid_job").val();
            switch (paid) {
                case "":
                    $(
                        "label[for=id_name_of_company_paid],#id_name_of_company_paid"
                    ).hide();
                    break;
                case "0":
                    $(
                        "label[for=id_name_of_company_paid],#id_name_of_company_paid"
                    ).show();
                    break;
                case "1":
                    $(
                        "label[for=id_name_of_company_paid],#id_name_of_company_paid"
                    ).hide();
                    break;
                default:
                    $(
                        "label[for=id_name_of_company_paid],#id_name_of_company_paid"
                    ).hide();
            }
        });
    });
});
//************************************************************************************ */
// hide volations case in the admin page
// $( document ).ready( function() {
// $(function () {
//   if ($('#id_violations').val() =='1') {
//     $('label[for=id_kind_of_violation_1],#id_kind_of_violation_1').hide();
//     $('label[for=id_date_of_violations_1],#id_date_of_violations_1').hide();
//     $('.datetimeshortcuts').hide();
// }
//       $('#id_violations').change(function () {
//       var violation=$('#id_violations').val()
//       switch(violation) {
//         case '0':
//           $('label[for=id_kind_of_violation_1],#id_kind_of_violation_1').show();
//           $('label[for=id_date_of_violations_1],#id_date_of_violations_1').show();
//           $('.datetimeshortcuts').show()
//           break;
//         case '1':
//          $('label[for=id_kind_of_violation_1],#id_kind_of_violation_1').hide();
//          $('label[for=id_date_of_violations_1],#id_date_of_violations_1').hide();
//          $(this)('.datetimeshortcuts').hide()
//           break;
//         default:
//         $('label[for=id_kind_of_violation_1],#id_kind_of_violation_1').hide();
//          $('label[for=id_date_of_violations_1],#id_date_of_violations_1').hide();
//          $('.datetimeshortcuts').hide();

//       }

//     });
// });
// });
//****************************************************************   */
// paid show and hide
$(document).ready(function () {
    $(function () {
        if ($("#id_paid_job").val() == "1") {
            $("label[for=id_name_of_company_paid],#id_name_of_company_paid").hide();
        }
        $("#id_paid_job").change(function () {
            var paid = $("#id_paid_job").val();
            switch (paid) {
                case "":
                    $(
                        "label[for=id_name_of_company_paid],#id_name_of_company_paid"
                    ).hide();
                    break;
                case "0":
                    $(
                        "label[for=id_name_of_company_paid],#id_name_of_company_paid"
                    ).show();
                    break;
                case "1":
                    $(
                        "label[for=id_name_of_company_paid],#id_name_of_company_paid"
                    ).hide();
                    break;
                default:
                    $(
                        "label[for=id_name_of_company_paid],#id_name_of_company_paid"
                    ).hide();
            }
        });
    });
});

//**************************************************************************************** */
// hide and show the media member block
$(document).ready(function () {
    $(function () {
        $("div.fieldBox.field-details").hide();
        if ($("#id_org_memeber").val() == "1") {
            $("div.fieldBox.field-details").show();
        }
        $(" #id_org_memeber").change(function () {
            var paid = $("#id_org_memeber").val();
            switch (paid) {
                case "":
                    $("div.fieldBox.field-details").hide();
                    break;
                case "0":
                    $("div.fieldBox.field-details").hide();
                    break;
                case "1":
                    $("div.fieldBox.field-details").show();
            }
        });
    });
});

///////////////////////////////////////////////////////////::
$(document).ready(function () {
    $(function () {
        // $('.support').hide();
        // $('.supportchild').hide();
        $("#id_checking-0-result_of_verfication").change(function () {
            var support = $("#id_checking-0-result_of_verfication").val();
            switch (support) {
                case "":
                    $(".support").hide();
                    $(".supportchild").hide();
                    $(".supportchild_cost").hide();
                    break;
                case "0":
                    $(".support").Show();
                    $(".supportchild").show();
                    $(".supportchild_cost").show();
                    break;
                case "1":
                    $(".support").hide();
                    $(".supportchild").hide();
                    $(".supportchild_cost").hide();
                    break;
                default:
                    $(".support").hide();
                    $(".supportchild").hide();
            }
        });
    });
});

//   });
//   });
// // function to hide the cost from supportchils
// $( document ).ready( function() {
//   $(function () {
//     $('.supportchild_cost').hide();
//   // $('.abcdefgh').hide();
//       $('#id_type_of_dmande').change(function () {
//         $('.supportchild_cost').hide();
//         // $('.abcdefgh').hide();
//           if (this.options[this.selectedIndex].value =='0') {

//             $('.supportchild_cost').show();
//           }

//       });

//   });
//   });

// function to note the years of experinces
$(document).ready(function () {
    $(function () {
        // $('.abcdefgh').hide();
        $("#id_checking-0-number_of_year_exprince").change(function () {
            var years_exp = $("#id_checking-0-number_of_year_exprince").val();
            switch (years_exp) {
                case "0":
                    $("#id_checking-0-note_of_year_experince").val("1");
                    break;
                case "1":
                    $("#id_checking-0-note_of_year_experince").val("2");
                    break;
                case "2":
                    $("#id_checking-0-note_of_year_experince").val("3");
                    break;
                case "3":
                    $("#id_checking-0-note_of_year_experince").val("0");
                    break;

                default:
                    $("#id_checking-0-note_of_year_experince").val("0");
            }
        });
    });
});
//function to note the step2
$(document).ready(function () {
    $(function () {
        // $('.abcdefgh').hide();
        $("#id_checking-0-rspect_legal_coppyright").change(function () {
            var coppy_right = $("#id_checking-0-rspect_legal_coppyright").val();
            switch (coppy_right) {
                case "0":
                    $("#id_checking-0-mark_rspect_legal_coppyright").val("1");
                    break;
                case "1":
                    $("#id_checking-0-mark_rspect_legal_coppyright").val("0");
                    break;
                default:
                    $("#id_checking-0-mark_rspect_legal_coppyright").val("0");
            }
        });
    });
});
////////////////////////////////////
$(document).ready(function () {
    $(function () {
        // $('.abcdefgh').hide();
        $("#id_checking-0-rspect_coppyright").change(function () {
            var coppy_right = $("#id_checking-0-rspect_coppyright").val();
            switch (coppy_right) {
                case "0":
                    $("#id_checking-0-mark_rspect_coppyright").val("1");
                    break;
                case "1":
                    $("#id_checking-0-mark_rspect_coppyright").val("0");
                    break;
                default:
                    $("#id_checking-0-mark_rspect_coppyright").val("0");
            }
        });
    });
});
////////////////////////////////////////////////////
$(document).ready(function () {
    $(function () {
        // $('.abcdefgh').hide();
        $("#id_checking-0-rspect_right_human").change(function () {
            var coppy_right = $("#id_checking-0-rspect_right_human").val();
            switch (coppy_right) {
                case "0":
                    $("#id_checking-0-mark_rspect_right_human").val("1");
                    break;
                case "1":
                    $("#id_checking-0-mark_rspect_right_human").val("0");
                    break;
                default:
                    $("#id_checking-0-mark_rspect_right_human").val("0");
            }
        });
    });
});

//all for notes and export values from parent model
$(document).ready(function () {
    //for fill field
    //$('##id_first_name').removeAttr('readonly');
    // $("#id_checking-0-tiitle_of_state").val(
    //     $("#id_first_name").val() +
    //     " " +
    //     $("#id_last_name").val() +
    //     " " +
    //     "من" +
    //     "  " +
    //     $("#id_city").val()
    // );

    $('#id_checking-0-tiitle_of_state').addClass('w-50');
    $('#id_checking-0-tiitle_of_state').val(
        $('#id_profile option:selected').text()
    );



    //$('#id_first_name').add('readonly');
    //family number into family state
    $("#id_checking-0-family_state_1").val($("#id_number_kids").val());
    $("#id_checking-0-first_recmond_name").val($("#id_recmond_1").val());
    $("#id_checking-0-second_recmond_name").val($("#id_recmond_2").val());

    //here is you can write placeholder for all fields that exist in inline form
    // $("#id_checking-0-cruntly_adre").attr('placeholder', 'hello' )
    //$("#id_checking-0-confirm_stat").val($('#id_type_of_dmande').value());
    //This is a simple way of getting the DAYS between two dates**

    $("#id_checking-0-number_of_year_exprince").val($("#id_start_date").val());

    var demand = $("#id_type_of_dmande").val();
    var edu_point = $("#id_education_level").val();
    var media_memeber = $("#id_org_memeber").val();
    var medical_state = $("#id_medical_state_q").val();
    var paid1_job = $("#id_experience").val();
    var violation_q = $("#id_violations").val();

    var a = parseInt($("#id_checking-0-member_in_journal").val());
    var b = parseInt($("#id_checking-0-educatton_level_1").val());
    var c = parseInt($("#id_checking-0-medical_state").val());
    var d = parseInt($("#id_checking-0-note_paid_job").val());
    var f = parseInt($("#id_checking-0-mark_rspect_right_human").val());
    var t = parseInt($("#id_checking-0-mark_rspect_coppyright").val());
    var g = parseInt($("#id_checking-0-rspect_legal_coppyright").val());
    var h = parseInt($("#id_checking-0-note_of_year_experince").val());

    $("#id_checking-0-total_of_note").val(a + b + c + d + h + f + t);

    //give the type of the demande note
    switch (demand) {
        case "0":
            $("#id_checking-0-confirm_stat").val("دعم معيش");
            break;
        case "1":
            $("#id_checking-0-confirm_stat").val("إيجاد فرصة عمل");
            break;
        case "2":
            $("#id_checking-0-confirm_stat").val("خروج آمن");
            break;
        case "3":
            $("#id_checking-0-confirm_stat").val(
                "خروج دعم ملف اللجوء - تأشيرات خروج"
            );
            break;
        case "4":
            $("#id_checking-0-confirm_stat").val("دعم تقني وبطاقات صحفية");
            break;
        case "5":
            $("#id_checking-0-confirm_stat").val("دعم طبي");
            break;
        case "6":
            $("#id_checking-0-confirm_stat").val("غير ذلك");
            break;
        default:
            $("#id_checking-0-confirm_stat").val("0");
    }
    //give the eduction level note
    switch (edu_point) {
        case "1":
            $("#id_checking-0-educatton_level_1").val("0");
            break;
        case "2":
            $("#id_checking-0-educatton_level_1").val("1");
            break;
        case "3":
            $("#id_checking-0-educatton_level_1").val("2");
            break;
        case "4":
            $("#id_checking-0-educatton_level_1").val("3");
            break;
        default:
            $("#id_checking-0-educatton_level_1").val("0");
    }
    //give note for the member ship in media commity
    switch (media_memeber) {
        case "0":
            $("#id_checking-0-member_in_journal").val("0");
            break;
        case "1":
            $("#id_checking-0-member_in_journal").val("1");
            break;

        default:
            $("#id_checking-0-member_in_journal").val("0");
    }
    switch (medical_state) {
        case "0":
            $("#id_checking-0-medical_state").val("0");
            break;
        case "1":
            $("#id_checking-0-medical_state").val("1");
            break;

        default:
            $("#id_checking-0-medical_state").val("0");
    }
    switch (paid1_job) {
        case "0":
            $("#id_checking-0-note_paid_job").val("0");
            break;
        case "1":
            $("#id_checking-0-note_paid_job").val("1");
            break;

        default:
            $("#id_checking-0-note_paid_job").val("0");
    }
    switch (violation_q) {
        case "0":
            $("#id_checking-0-hase_violants").val("0");
            break;
        case "1":
            $("#id_checking-0-hase_violants").val("1");
            break;

        default:
            $("#id_checking-0-hase_violants").val("0");
    }

});
django.jQuery;