import React from "react";
import styles from "../styles/BirthdayRow.module.css"

function BirthdayRow({ birthday, onDelete }) {
  console.log(birthday);
  console.log(onDelete);
  return (
    <div className={styles.birthday_row}>
      <p>{birthday.name}</p>
      <p>{birthday.date.month} / {birthday.date.day}</p>
      <div className={styles.button_container}><button className={styles.button} onClick={() => onDelete(birthday.name)}>{'\u2715'}</button></div>
    </div>
  );
}

function BirthdayRowHeader() {
  return (
    <div className={styles.birthday_row}>
      <p>Name</p>
      <p>Date</p>
      <p></p>
    </div>
  );
}

function AddRow() {
  return (
    <div className={styles.birthday_row}>
      <p> </p>
      <p>Date</p>
      <p> </p>
    </div>
  );
}

export {BirthdayRowHeader, BirthdayRow, AddRow};

