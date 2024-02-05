function validate() {
    var usn = document.getElementById("usn").value;
    var check = /^[1-4][A-Z]{2}\d{2}[A-Z]{2}\d{3}$/;
    console.log("Checking USN");
    var res = check.test(usn);

    if (!res) {
        alert("Invalid USN FORMAT");
        return;
    } else {
        var sem = document.getElementById("semester").value;
        alert("Your USN is " + usn + "\nSemester: " + sem);
    }

    console.log("Verification Done");
}
