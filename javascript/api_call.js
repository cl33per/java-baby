
var api_updateLevelTwo = function () { //"#cf_example", "cf_example", variable: @example@}
    console.log('Updating Level 2');
    console.log('Updating => ', result);
    var request = $.ajax({
        url: "https://fedramp.mod.udpaas.com/API/1/user/",
        type: "POST",
        data: {
            companyid: "1541170",
            apitoken: "BGBzdQVGcnA1R3JUblVCXAVkfV0BaXcECzEPCQ~~",
            alias:"fedramp",
            username: "udpaas_api_user@etranservices.com",
            password: "1234567890",
            jsonrset: JSON.stringify(result)
        },
        dataType: "html"
    });
    request.done(function (data) {
        json = JSON.parse(data);
        console.log('Response from Lv2 API Post RoC: ', json);
    });
}