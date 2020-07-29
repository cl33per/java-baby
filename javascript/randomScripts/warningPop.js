<script>
//* require wp-plugin js file
var popUp = "https://whinsec.org/wp-content/plugins/popup-by-supsystic/modules/popup/js/frontend.popup.js?ver=1.10.1"
jQuery.getScript(popUp,
    // TODO: research onClick vs live click fun call
    jQuery('a').live('click', function (e) {
        // method tells the user agent that if the event does not get explicitly handled, its default action should not be taken as it normally would be.
        e.preventDefault();
        var url = jQuery(this).attr('href'),
            host = location.host;
        // If we find the host name within the URL, OR if we do not find http or https, meaning it is a relative internal link
        if (url.indexOf(host) > -1 || url.indexOf('http', 'https') == -1) {
            window.location.href = url;
        } else {
            var warn = confirm('You are leaving WHINSEC.org and entering an external website. Links to non-U.S. government sites or services are solely for your convenience. The appearance of hyperlinks to non-government Websites from the WHINSEC.org Website does not constitute endorsement by the Department of Defense, The U.S. Army, Fort Benning, Western Hemisphere Institute for Security Cooperation (WHINSEC) or any of its employees or the sponsors of the information, products or services the site contains.\

For other than authorized activities such as military exchanges and Morale, Welfare and Recreation (MWR) sites, DoD/the Army/Fort Benning/WHINSEC do not exercise any editorial control over and responsibility for the information you may find at these locations. Such links are provided consistent with the stated purpose of this DoD Website.');
            if (warn == true) {
                 window.location.href = url, '_blank';
             } else {
                 e.preventDefault;
            }
        }
    }));
</script>

<script>
    //* require wp-plugin js file
    jQuery('a').live('click', function (e) {
                e.preventDefault();
        // method tells the user agent that if the event does not get explicitly handled, its default action should not be taken as it normally would be.
        var url = jQuery(this).attr('href'),
            host = location.host;
        // If we find the host name within the URL, OR if we do not find http or https, meaning it is a relative internal link
        if (url.indexOf(host) > -1 || url.indexOf('http', 'https') == -1) {
            // window.location.href = url;
        } else {
            var warn = confirm(
                'You are leaving WHINSEC.org and entering an external website. Links to non-U.S. government sites or services are solely for your convenience. The appearance of hyperlinks to non-government Websites from the WHINSEC.org Website does not constitute endorsement by the Department of Defense, The U.S. Army, Fort Benning, Western Hemisphere Institute for Security Cooperation (WHINSEC) or any of its employees or the sponsors of the information, products or services the site contains.\n\nFor other than authorized activities such as military exchanges and Morale, Welfare and Recreation (MWR) sites, DoD/the Army/Fort Benning/WHINSEC do not exercise any editorial control over and responsibility for the information you may find at these locations. Such links are provided consistent with the stated purpose of this DoD Website.'
            );
            if (warn == true) {
                window.open(url, '_blank');
            } else {
                e.preventDefault;
            }
        }
    });
</script>