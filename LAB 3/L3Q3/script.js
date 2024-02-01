function extractPhoneNumber() {
    var phoneNumberInput = document.getElementById("phoneNumberInput").value;
    var extractedInfo = extractInfo(phoneNumberInput);

    document.getElementById("areaCodeOutput").value = extractedInfo.areaCode;
    document.getElementById("phoneNumberOutput").value = extractedInfo.phoneNumber;
}

function extractInfo(phoneNumber) {
    var tokens = phoneNumber.replace(/[^\d]/g, '').split('');

    var areaCode = tokens.slice(0, 2).join('');
    var phoneNumber = tokens.slice(2).join('');

    return {
        areaCode: areaCode,
        phoneNumber: phoneNumber
    };
}

function clearInputAndOutput() {
    document.getElementById("phoneNumberInput").value = "";
    document.getElementById("areaCodeOutput").value = "";
    document.getElementById("phoneNumberOutput").value = "";
}
