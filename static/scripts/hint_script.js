// This script returns the relevant hints for Hints.html

$(document).ready(function() {
    $('.hint-button').on('click', function() {
        const button = $(this);
        const questionId = button.closest('.question-hints').data('question-id');
        let hintLevel = parseInt(button.attr('data-hint-level'));

        $.post('/get_hint', { question_id: questionId, hint_level: hintLevel }, function(response) {
            if (response.hint) {
                const hintsList = button.closest('.question-hints').find('.hints-list');
                hintsList.append(`<li>${response.hint}</li>`);

                // Increment the hint level for the button
                button.attr('data-hint-level', hintLevel + 1);
            } else {
                alert('No more hints available for this question.');
            }
        });
    });



    // This script tells the user on button press what prerequisite clues are required
    $('.required-button').on('click', function() {
        const button = $(this);
        const questionId = button.closest('.question-hints').data('question-id');

        $.post('/get_required_hint', { question_id: questionId }, function(response) {
            if (response.RequiredHint) {
                const requiredPlaceholder = button.closest('.question-hints').find('.required-hint');
                requiredPlaceholder.text(response.RequiredHint); // Display the required hint
            }
        });
    });
});
