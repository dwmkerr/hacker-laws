$(document).ready(function() {
    $("h1, h2, h3, h4, h5, h6").each(function() {
        var $heading = $(this);
        var headingId = $heading.attr("id") || $heading.text().trim().toLowerCase().replace(/\s+/g, "-");

        // Ensure a unique ID
        $heading.attr("id", headingId);

        // Create the anchor link
        var $anchor = $('<a>')
            .attr("href", "#" + headingId)
            .addClass("header-link")
            .html("#");

        // Append to the heading
        $heading.append($anchor);
    });

    //  Bootstrap requires that blockquote elements have the 'blockquote' class.
    $('blockquote').addClass('blockquote').addClass('.quote');
});
