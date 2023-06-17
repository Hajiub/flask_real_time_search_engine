$(document).ready(function() {
    $('#search-input').on('input', function() {
        var keyword = $(this).val();
        $.ajax({
            url: '/search',                      
            type: 'POST',                          
            contentType: 'application/json',      
            data: JSON.stringify({ 'keyword': keyword }), 
            success: function(response) {
                var results = response.results;  

                
                var listItems = results.map(function(car) {
                    return `<li>
                                <a href="${car.url}">${car.make}, ${car.model}, ${car.price}</a>
                            </li>`;
                });
                $('#search-results').html(listItems.join(''));
            }
        });
    });
});