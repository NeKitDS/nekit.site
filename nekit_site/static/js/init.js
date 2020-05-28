(function($) {
    $(function() {
        // enable sidebar navigation
        $(".sidenav").sidenav();
    });
})(jQuery);

// is it alright? ~ nekit

function theme_switch() {
    let switch_dict = {"dark": "light", "light": "dark"};
    document.body.setAttribute(
        "data-theme", switch_dict[document.body.getAttribute("data-theme")]
    );
}
