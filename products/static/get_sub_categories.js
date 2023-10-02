$(document).ready(function() {
    $('[name="category"]').change(function() {
        const selectedValue = $(this).val();

        $.ajax({
            url: `/get_sub_categories/?value=${selectedValue}`,
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                let subCategoryField = $('[name="sub_category"]');
                subCategoryField.empty();

                $.each(data, function(index, option) {
                    field2.append($('<option>', {
                        value: option.value,
                        text: option.label
                    }));
                });
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });
});
