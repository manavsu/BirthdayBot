import React from "react";

function GetBirthdayData(setBirthdays) {
    fetch('http://127.0.0.1:5000/birthdays').then((data) => data.json()).then((metaData) => setBirthdays(metaData))
}