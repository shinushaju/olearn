$(document).ready(function () {
    var max_fields = 25; //maximum input boxes allowed
    var wrapper = $(".section-container-box"); //Fields wrapper
    var add_button = $(".add-section-btn"); //Add button ID

    var count = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        e.preventDefault();
        if (count < max_fields) { //max input box allowed
            count++; //text box increment
            $(wrapper).append(`
            <div class="w3-animate-opacity section-container">
            <span class="w3-section" style="font-weight: 500;color: #666666;">Add a Section </span>
            <a href="#" style="text-decoration:none" class="w3-right w3-text-gray remove_section"><i class="bi bi-trash"></i></a>
            <br/><br/>
            <label class="required-field">Section Title</label>
            <input type="text" class="w3-margin-bottom" name="section_title[]" placeholder="Enter section title..." required/>
            <label class="required-field">Section Outcome</label>
            <textarea type="text" name="section_outcome[]" placeholder="Enter section outcome..." rows="2" required></textarea>
            </div><hr/>`);
        }
    });

    $(wrapper).on("click", ".remove_section", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); count--;
    })
});

$(document).ready(function () {

    var max_fields = 25; //maximum input boxes allowed
    var lecture_main = $(".lecture-box").find(".lecture-main-box"); //Fields wrapper

    $.each(lecture_main, function (index, value) {

        var add_button = $(value).find('.add-lecture-btn');
        var lecture_wrapper = $(value).find(".lecture-container-box");
        var section_id = $(lecture_wrapper).attr("id")
        var count = 1; //initlal text box count
        $(add_button).click(function (e) { //on add input button click
            e.preventDefault();

            if (count < max_fields) { //max input box allowed
                count++; //text box increment
                $(lecture_wrapper).append(`
                <div class="w3-animate-opacity lecture-container">
                <hr/>
                <span style="font-weight: 500;color:#666666;">Add a Lecture</span>
                <a href="#" style="text-decoration:none" class="w3-right w3-text-gray remove_lecture"><i class="bi bi-trash"></i></a>
                <input type="number" class="w3-hide" name="section_id[]" value="${section_id}"/>
                <div class="input w3-container w3-margin-top">
                    <label class="required-field">Lecture Title</label>
                    <input type="text" class="w3-margin-bottom" name="lecture_title[]"
                        placeholder="Enter lecture name..." required/>
                </div>
    
                <div class="w3-row-padding">
                    <div class="w3-half">
                        <label class="required-field">Link to Lecture</label>
                        <input type="url" class="w3-margin-bottom" name="lecture_link[]"
                            placeholder="Enter lecture link..." required/>
                    </div>
                    <div class="w3-half">
                        <label class="required-field">Lecture Duration in Minutes</label>
                        <input type="number" min="0" class="w3-margin-bottom"
                            name="lecture_duration[]" placeholder="Enter Duration..." required/>
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

/*
$(document).ready(function () {
    var max_fields = 25; //maximum input boxes allowed
    var wrapper = $(".accordionWrapper"); //Fields wrapper
    var add_button = $(".add-section-btn"); //Add button ID

    var count = 1; //initlal text box count
    $(add_button).click(function (e) { //on add input button click
        console.log("clicked")
        e.preventDefault();
        if (count < max_fields) { //max input box allowed
            count++; //text box increment
            $(wrapper).append(`
            <div class="w3-section w3-animate-opacity">

            <div class="w3-margin-bottom">
                <label class="w3-small">Section Title</label>
                <input type="text" placeholder="Enter section title..." name="section_title" required>
            </div>
            <div class="w3-margin-bottom">
                <label class="w3-small">Section Outcome</label>
                <textarea type="text" placeholder="Enter section outcome..."
                    name="section_outcome" rows="2"
                    required></textarea>
            </div>
            <br>
            <a href="#" style="text-decoration:none" class="w3-right w3-text-gray remove_new_section"><i class="bi bi-trash"></i></a>
            <br>
            <hr>
            </div>`);
        }
    });

    $(wrapper).on("click", ".remove_new_section", function (e) { //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); count--;
    })
});
*/