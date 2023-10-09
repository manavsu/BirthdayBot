import React from "react";

function GetBirthdayData(setBirthdays) {
    fetch('http://127.0.0.1:5000/birthdays').then((data) => data.json()).then((metaData) => setBirthdays(metaData));
}

function DeleteBirthdayAndReload(name, setBirthdays) {
    fetch('http://127.0.0.1:5000/birthdays/' + name, {method: 'DELETE'}).then(() => GetBirthdayData(setBirthdays));
}

function AddBirthday(name, month, day, setBirthdays) {
    fetch('http://127.0.0.1:5000/birthdays/' + name + '/' + month + '/' + day, {method: 'POST'}).then(() => GetBirthdayData(setBirthdays));
}

export {GetBirthdayData, DeleteBirthdayAndReload, AddBirthday}