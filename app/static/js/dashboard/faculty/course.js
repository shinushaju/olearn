$(document).ready(function () {
    var max_fields = 25; //maximum input boxes allowed
    var wrapper = $(".section-container-box"); //Fields wrapper
    var add_button = $(".add-section-btn"); //Add button ID

    var count = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (count < max_fields) { //max input box allowed
            count++; //text box increment
            $(wrapper).append(`<div class="w3-animate-opacity section-container"><hr/><span class="w3-margin-bottom w3-left" style="font-weight: 500;">Section ${count}</span><a href="#" style="text-decoration:none" class="w3-right w3-text-gray remove_section"><i class="bi bi-trash"></i></a><input type="text" name="section_title[]" placeholder="Enter section title..."/>
            <textarea class="w3-margin-top" type="text" name="section_outcome[]" placeholder="Enter section outcome..." rows="2"></textarea></div>`);
        }
    });

    $(wrapper).on("click", ".remove_section", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); count--;
    })
});




$(document).ready(function () {

    var max_fields = 25; //maximum input boxes allowed
    var lecture_main = $(".section-box").find(".lecture-main-box"); //Fields wrapper

    $.each(lecture_main, function (index, value) {

        var add_button = $(value).find('.add-lecture-btn');
        var lecture_wrapper = $(value).find(".lecture-container-box");

        var count = 1; //initlal text box count
        $(add_button).click(function (e) { //on add input button click
            e.preventDefault();

            if (count < max_fields) { //max input box allowed
                count++; //text box increment
                $(lecture_wrapper).append(`
                <div class="lecture-container">
                <hr/>
                <span style="font-weight: 500;">Lecture ${count}</span>
                <a href="#" style="text-decoration:none" class="w3-right w3-text-gray remove_lecture"><i class="bi bi-trash"></i></a>
                <div class="w3-container w3-margin-top">
                    <input type="text" class="w3-margin-bottom" name="lecture_title[]"
                        placeholder="Give lecture name..." />
                </div>
    
                <div class="w3-row-padding">
                    <div class="w3-half">
                        <input type="url" class="w3-margin-bottom" name="lecture_link[]"
                            placeholder="Give lecture link..." />
                    </div>
                    <div class="w3-half">
                        <input type="number" min="0" class="w3-margin-bottom"
                            name="lecture_duration[]" placeholder="Lecture Duration..." />
                    </div>
                </div>
            </div>
                `);
            }
        });

        $(lecture_wrapper).on("click", ".remove_lecture", function (e) { //user click on remove text
            e.preventDefault(); $(this).parent('div').remove(); --count;
        })

    });

});


